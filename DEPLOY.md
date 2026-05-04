# Ground App Deployment Guide

This guide covers running Ground locally, deploying to Render, and building the Android TWA (Trusted Web Activity) wrapper.

## Prerequisites

- Python 3.9+
- Node.js 16+ (for frontend builds, if applicable)
- Android SDK (for TWA builds)
- Java 11+ (for Gradle builds)
- A Render account (for cloud deployment)

## Local Development

### 1. Install Python dependencies

```bash
cd /path/to/ground-app
pip install -r requirements.txt
```

### 2. Run the app

```bash
python webapp.py
```

The app will start on `http://localhost:8081` by default.

### 3. Verify the app is running

Open a browser and navigate to `http://localhost:8081`. You should see the Ground reflection interface.

## Deploying to Render

Ground follows the same deployment pattern as the Dream Coherence app.

### 1. Create a Render account

Visit [render.com](https://render.com) and sign up if you don't already have an account.

### 2. Connect your Git repository

- Go to **Dashboard** → **New** → **Web Service**
- Select your GitHub/GitLab repository containing the Ground app
- Authorize Render to access your repo

### 3. Configure the Render service

**Service settings:**
- **Name:** `ground-moral` (or your preferred name)
- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python webapp.py`
- **Plan:** Free tier (for development) or Starter+ (for production)

**Environment variables:**
- Add any required `.env` variables to Render's environment settings
- For local development, copy `.env.example` to `.env` and fill in your values

### 4. Deploy

Once configured, Render will automatically deploy on every git push to your main branch.

**Deployment URL:** `https://ground-moral.onrender.com` (adjust the subdomain to match your service name)

### 5. Configure a custom domain (optional)

In your Render dashboard:
- Go to your service → **Settings** → **Custom Domain**
- Point your domain to the Render service using DNS records

## Building the Android TWA

### Overview

The Android TWA (Trusted Web Activity) is a lightweight wrapper that launches Ground in a fullscreen, app-like experience on Android without browser UI chrome.

### 1. Prerequisites for TWA build

- **Android SDK:** Install via Android Studio or command line
- **Java 11+:** Required by Gradle
- **Gradle:** Managed by the gradlew wrapper (no separate install needed)

### 2. Generate a keystore for signing

A keystore is required to sign the APK for release. Generate a fresh keystore for Ground:

```bash
cd /path/to/ground-app/android-twa

# Generate a new keystore (only do this once)
keytool -genkey -v -keystore ground-keystore.jks \
  -keyalg RSA -keysize 2048 \
  -validity 10000 \
  -alias ground-key

# When prompted:
# - Enter a strong password (save this!)
# - Provide your name, organization, and location
# - Confirm the password
```

**Important:** Store the keystore file and password securely. You'll need it for all future APK builds.

### 3. Set up Gradle signing configuration

Create a `gradle.properties` file in `android-twa/` with signing credentials:

```properties
android.useAndroidX=true
org.gradle.jvmargs=-Xmx2048m

# Signing config (for release builds)
KEYSTORE_FILE=/full/path/to/ground-keystore.jks
KEYSTORE_PASSWORD=your_keystore_password
KEY_ALIAS=ground-key
KEY_PASSWORD=your_key_password
```

**Security note:** Do not commit this file to version control. Add it to `.gitignore`:
```
android-twa/gradle.properties
```

### 4. Update the web URL (if different)

In `app/build.gradle`, update the `hostName` and `defaultUrl` if your Render deployment uses a different domain:

```gradle
manifestPlaceholders = [
    hostName: "your-domain.onrender.com",
    defaultUrl: "https://your-domain.onrender.com",
    launcherName: "Ground",
    assetStatements: '[{ "relation": ["delegate_permission/common.handle_all_urls"], "target": { "namespace": "web", "site": "https://your-domain.onrender.com" } }]'
]
```

### 5. Build the APK

```bash
cd /path/to/ground-app/android-twa

# Debug build (for testing on emulator/device)
./gradlew assembleDebug

# Release build (for Play Store submission)
./gradlew assembleRelease
```

**Output locations:**
- Debug APK: `app/build/outputs/apk/debug/app-debug.apk`
- Release APK: `app/build/outputs/apk/release/app-release.apk`

### 6. Test on Android device or emulator

```bash
# Install debug APK on connected device
./gradlew installDebug
```

Or use Android Studio's device manager to run on an emulator.

## Setting Up Digital Asset Links for TWA Verification

TWA verification links the Android app to your web domain. This requires a `assetlinks.json` file.

### 1. Generate your app's SHA-256 fingerprint

```bash
# For debug keystore (testing)
keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey

# For release keystore
keytool -list -v -keystore /path/to/ground-keystore.jks -alias ground-key
```

Look for the line starting with `SHA256:`. Copy the full value.

### 2. Create the assetlinks.json file

On your web server (where Ground is deployed), create:
```
/.well-known/assetlinks.json
```

Contents (replace `PACKAGE_NAME` and `SHA256_HASH` with your actual values):

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.ground.moral",
    "sha256_cert_fingerprints": ["YOUR_SHA256_FINGERPRINT_HERE"]
  }
}]
```

### 3. Verify the assetlinks.json

Test that your web server serves the file correctly:

```bash
curl https://ground-moral.onrender.com/.well-known/assetlinks.json
```

You should see the JSON response without errors.

### 4. Rebuilding after assetlinks.json setup

Once the assetlinks.json is in place:

1. Rebuild the APK with your release keystore
2. Install it on a device
3. The app will now launch as a full TWA (no browser UI)

If verification fails, the app will fall back to a Custom Tab (shows minimal browser bar).

## Troubleshooting

### "Gradle not found" or build failures

Ensure you have Java 11+ and the Android SDK installed. Run:
```bash
./gradlew --version
```

### APK installation fails on device

- Ensure your device is connected: `adb devices`
- Grant USB debugging permissions on the device
- Try: `./gradlew installDebug -x lint`

### TWA loads as Custom Tab instead of fullscreen

This means assetlinks.json verification failed. Check:
1. File is at `https://your-domain.com/.well-known/assetlinks.json`
2. SHA256 fingerprint in assetlinks.json matches your signing key
3. No HTTPS or domain mismatches in the manifest

### Web app not loading in TWA

- Check that your Render deployment URL is accessible
- Verify the URL in `LauncherActivity.java` matches your deployment domain
- Check browser console in Android Studio's Device Monitor for errors

## Production Checklist

Before releasing to the Play Store:

- [ ] Update version code and name in `app/build.gradle`
- [ ] Ensure assetlinks.json is deployed and verified
- [ ] Test the release APK on multiple devices
- [ ] Configure app signing in Play Console
- [ ] Create app listing with screenshots and description
- [ ] Set up pricing and distribution settings
- [ ] Submit for review

## Support and Updates

For updates to Ground or the TWA wrapper:

1. Update the web app on Render (git push triggers auto-deploy)
2. For Android app updates, rebuild and submit new APK to Play Store
3. Version codes in `build.gradle` must increment with each release

---

**Last updated:** April 2026
