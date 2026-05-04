# Ground TWA Setup Checklist

This checklist ensures your Ground TWA is properly configured for development, testing, and release.

## Initial Setup

- [ ] **Java 11+ installed**
  ```bash
  java -version  # Should show Java 11 or higher
  ```

- [ ] **Android SDK installed**
  ```bash
  echo $ANDROID_HOME  # Should point to your Android SDK
  ```

- [ ] **gradle/wrapper directory exists**
  - Contains `gradle-wrapper.properties` (✓ included)

## Configuration Files

- [ ] **settings.gradle**
  - Project name set to "Ground" ✓

- [ ] **build.gradle (root)**
  - Android Gradle plugin 8.2.2 ✓
  - Repositories configured ✓

- [ ] **app/build.gradle**
  - Package name: `com.ground.moral` ✓
  - App name: "Ground" ✓
  - Web URL: `ground-moral.onrender.com` ✓
  - Signing configuration (for release) ✓

- [ ] **AndroidManifest.xml**
  - Package name matches build.gradle ✓
  - INTERNET permission included ✓
  - LauncherActivity configured ✓
  - Deep link intent filters set up ✓
  - Asset statements configured ✓

- [ ] **LauncherActivity.java**
  - Package: `com.ground.moral` ✓
  - TWA implementation complete ✓
  - Custom Tab fallback included ✓
  - URL points to correct domain ✓

- [ ] **strings.xml**
  - App name: "Ground" ✓

- [ ] **styles.xml**
  - Dark theme applied (#0a0a1a) ✓
  - Status and nav bars configured ✓
  - Launch theme defined ✓

- [ ] **launch_background.xml**
  - Splash screen color set to #0a0a1a ✓

- [ ] **proguard-rules.pro**
  - Browser and app classes preserved ✓

- [ ] **.gitignore**
  - Keystores excluded ✓
  - gradle.properties excluded ✓
  - Build artifacts excluded ✓

## Before First Build

- [ ] **Create gradle.properties**
  - Copy from `gradle.properties.example`
  - Add actual keystore path
  - Add passwords (keep private!)

- [ ] **Update web domain (if needed)**
  - If using different domain than `ground-moral.onrender.com`
  - Update in `app/build.gradle` manifest placeholders
  - Update in `LauncherActivity.java` DEFAULT_URI

## Debug Build & Testing

- [ ] **Run debug build**
  ```bash
  ./gradlew assembleDebug
  ```
  - Output: `app/build/outputs/apk/debug/app-debug.apk`

- [ ] **Install on device/emulator**
  ```bash
  ./gradlew installDebug
  ```

- [ ] **Test basic functionality**
  - App launches
  - Web content loads
  - No SSL/HTTPS errors

## Keystore Setup (for Release)

- [ ] **Generate keystore (one-time)**
  ```bash
  keytool -genkey -v -keystore ground-keystore.jks \
    -keyalg RSA -keysize 2048 -validity 10000 \
    -alias ground-key
  ```

- [ ] **Store keystore securely**
  - Backup to secure location
  - Record password safely
  - Do NOT commit to Git

- [ ] **Configure gradle.properties**
  - KEYSTORE_FILE path
  - KEYSTORE_PASSWORD
  - KEY_ALIAS
  - KEY_PASSWORD

## Digital Asset Links Setup

- [ ] **Get keystore SHA-256 fingerprint**
  ```bash
  keytool -list -v -keystore ground-keystore.jks -alias ground-key
  ```
  - Copy SHA256 line

- [ ] **Create .well-known/assetlinks.json**
  - Location: `https://ground-moral.onrender.com/.well-known/assetlinks.json`
  - Format: Correct JSON with your SHA256 fingerprint
  - Accessibility: Publicly accessible (no auth required)

- [ ] **Verify assetlinks.json**
  ```bash
  curl https://ground-moral.onrender.com/.well-known/assetlinks.json
  ```

- [ ] **Rebuild and test with release keystore**
  ```bash
  ./gradlew assembleRelease
  ```

## Release Build & Distribution

- [ ] **Version code updated**
  - Increment in `app/build.gradle` for each release

- [ ] **Version name updated**
  - Follow semantic versioning

- [ ] **Release APK built**
  ```bash
  ./gradlew assembleRelease
  ```
  - Output: `app/build/outputs/apk/release/app-release.apk`

- [ ] **Sign for Play Store**
  - Use your release keystore
  - Store APK safely

- [ ] **Create Play Console listing** (if releasing to Play Store)
  - App name: Ground
  - Package: com.ground.moral
  - Screenshots
  - Description
  - Category
  - Content rating

## Ongoing Maintenance

- [ ] **gradle.properties** never committed
  ```bash
  git status | grep gradle.properties  # Should show nothing
  ```

- [ ] **Keystore backed up**
  - Offline copy stored safely

- [ ] **Version code incremented** before each build

- [ ] **assetlinks.json updated** if changing signing keys

## Documentation

- [ ] **README.md** - Technical overview ✓
- [ ] **QUICKSTART.md** - Fast reference ✓
- [ ] **SETUP_CHECKLIST.md** - This document ✓
- [ ] **../DEPLOY.md** - Full deployment guide ✓

---

**Status:** Setup complete when all items are checked.

**Next steps:**
1. Run `./gradlew assembleDebug` to build
2. Test on device: `./gradlew installDebug`
3. For release, follow keystore and Digital Asset Links sections
