# Ground Android TWA (Trusted Web Activity)

This directory contains the Android Trusted Web Activity wrapper for Ground. It provides a lightweight native app shell that launches the Ground web app in fullscreen without browser UI chrome.

## Quick Start

### Prerequisites

- Android SDK (API 23+)
- Java 11+
- Gradle 8.5 (included via gradlew wrapper)

### Build and Test

```bash
# Debug build
./gradlew assembleDebug

# Install on connected device
./gradlew installDebug

# Release build (requires signing configuration)
./gradlew assembleRelease
```

## Project Structure

```
android-twa/
├── app/
│   ├── src/main/
│   │   ├── java/com/ground/moral/
│   │   │   └── LauncherActivity.java      # TWA launcher
│   │   ├── res/
│   │   │   ├── drawable/
│   │   │   │   └── launch_background.xml  # Splash screen
│   │   │   └── values/
│   │   │       ├── strings.xml
│   │   │       └── styles.xml
│   │   └── AndroidManifest.xml
│   ├── build.gradle                        # App-level config
│   └── proguard-rules.pro
├── gradle/
│   └── wrapper/
│       └── gradle-wrapper.properties        # Gradle version
├── build.gradle                            # Project-level config
├── settings.gradle                         # Project settings
├── gradle.properties                       # Gradle properties
└── gradlew / gradlew.bat                   # Gradle wrapper scripts
```

## Configuration

### Update the web URL

Edit `app/build.gradle` and update the manifest placeholders:

```gradle
manifestPlaceholders = [
    hostName: "your-domain.onrender.com",
    defaultUrl: "https://your-domain.onrender.com",
    launcherName: "Ground",
    assetStatements: '[{ ... }]'
]
```

### Signing for Release

1. Generate a keystore:
   ```bash
   keytool -genkey -v -keystore ground-keystore.jks \
     -keyalg RSA -keysize 2048 -validity 10000 \
     -alias ground-key
   ```

2. Create `gradle.properties` with signing credentials (not in git):
   ```properties
   KEYSTORE_FILE=/full/path/to/ground-keystore.jks
   KEYSTORE_PASSWORD=your_password
   KEY_ALIAS=ground-key
   KEY_PASSWORD=your_key_password
   ```

## Digital Asset Links Verification

For the app to launch as a full TWA (no browser UI), you must set up Digital Asset Links:

1. Get your release keystore's SHA-256 fingerprint:
   ```bash
   keytool -list -v -keystore ground-keystore.jks -alias ground-key
   ```

2. Create `/.well-known/assetlinks.json` on your web server:
   ```json
   [{
     "relation": ["delegate_permission/common.handle_all_urls"],
     "target": {
       "namespace": "android_app",
       "package_name": "com.ground.moral",
       "sha256_cert_fingerprints": ["YOUR_SHA256_HERE"]
     }
   }]
   ```

3. Verify it's accessible:
   ```bash
   curl https://ground-moral.onrender.com/.well-known/assetlinks.json
   ```

## Troubleshooting

- **Build fails:** Ensure Java 11+ is installed: `java -version`
- **APK won't install:** Try `./gradlew installDebug -x lint`
- **TWA loads as Custom Tab:** assetlinks.json verification failed (see above)

## See Also

- Parent deployment guide: `../DEPLOY.md`
- Android Custom Tabs docs: https://developer.chrome.com/docs/android/custom-tabs/
- Trusted Web Activity guide: https://developer.chrome.com/docs/android/trusted-web-activity/
