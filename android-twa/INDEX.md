# Ground Android TWA - File Index

Quick navigation for Ground's Android Trusted Web Activity project.

## Documentation (Start Here)

| Document | Purpose | Length |
|----------|---------|--------|
| [QUICKSTART.md](QUICKSTART.md) | 5-minute quick reference for building and testing | 82 lines |
| [README.md](README.md) | Project overview and directory structure | 120 lines |
| [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) | Verification checklist for complete setup | 194 lines |
| [../DEPLOY.md](../DEPLOY.md) | Full deployment guide (local, Render, APK, signing) | 270 lines |

## Build Configuration Files

| File | Purpose |
|------|---------|
| `settings.gradle` | Project name and module setup |
| `build.gradle` | Root-level build configuration |
| `gradle.properties` | Gradle VM args and Android settings |
| `gradle/wrapper/gradle-wrapper.properties` | Gradle version (8.5) |
| `app/build.gradle` | App-specific build config, signing setup, APK configuration |
| `app/proguard-rules.pro` | Code obfuscation rules for release builds |

## Application Source Code

| File | Purpose |
|------|---------|
| `app/src/main/java/com/ground/moral/LauncherActivity.java` | Main TWA launcher activity |
| `app/src/main/AndroidManifest.xml` | App manifest with TWA configuration |

## Android Resources

| File | Purpose |
|------|---------|
| `app/src/main/res/values/strings.xml` | String resources (app name) |
| `app/src/main/res/values/styles.xml` | Theme and styling (#0a0a1a dark theme) |
| `app/src/main/res/drawable/launch_background.xml` | Splash screen design |

## Configuration & Security

| File | Purpose | Contains Secrets |
|------|---------|------------------|
| `.gitignore` | Git exclusions (keystores, gradle.properties) | No |
| `gradle.properties.example` | Template for signing credentials | No |
| `gradle.properties` | Actual signing credentials (not in git) | Yes |

## Key Information

**Package Name:** `com.ground.moral`
**App Name:** Ground
**Web URL:** https://ground-moral.onrender.com
**Min Android:** API 23 (6.0)
**Target Android:** API 34 (14)
**Theme:** Dark (#0a0a1a)

## Common Tasks

### Build a Debug APK
```bash
./gradlew assembleDebug
# Output: app/build/outputs/apk/debug/app-debug.apk
```

### Install on Device
```bash
./gradlew installDebug
```

### Build Release APK
```bash
# First: copy gradle.properties.example to gradle.properties
# Then: add keystore path and passwords
./gradlew assembleRelease
# Output: app/build/outputs/apk/release/app-release.apk
```

### Get Keystore Fingerprint
```bash
keytool -list -v -keystore ground-keystore.jks -alias ground-key
# Copy the SHA256 line
```

## Setup Steps by Goal

### Goal: Test Debug Build
1. Read: [QUICKSTART.md](QUICKSTART.md) (2 min)
2. Run: `./gradlew assembleDebug` (5 min)
3. Run: `./gradlew installDebug` (2 min)

### Goal: Release to Play Store
1. Read: [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) (10 min)
2. Generate keystore: `keytool ...` (5 min)
3. Configure signing: Edit `gradle.properties` (2 min)
4. Build: `./gradlew assembleRelease` (5 min)
5. Read: [../DEPLOY.md](../DEPLOY.md) section "Production Checklist" (10 min)

### Goal: Enable Fullscreen TWA (no browser UI)
1. Read: [../DEPLOY.md](../DEPLOY.md) "Digital Asset Links" section (15 min)
2. Get SHA-256 from keystore
3. Create `/.well-known/assetlinks.json` on web server
4. Rebuild and test

## Security Best Practices

- Never commit `gradle.properties` (contains passwords)
- Never commit keystores (*.jks, *.p12)
- Use `gradle.properties.example` as a template
- Keep keystore password safe
- Backup keystore to offline storage
- Use unique keystore password
- Do not share keystore files

## Related Files (Parent Directory)

| File | Purpose |
|------|---------|
| `../DEPLOY.md` | Full deployment guide for Ground app |
| `../webapp.py` | Python Flask backend |
| `../requirements.txt` | Python dependencies |

## Gradle Wrapper

The project includes a Gradle wrapper (`gradlew` / `gradlew.bat`) for building without installing Gradle globally.

```bash
# On Mac/Linux
./gradlew --version

# On Windows
gradlew.bat --version
```

## Support

- Android TWA docs: https://developer.chrome.com/docs/android/trusted-web-activity/
- Custom Tabs: https://developer.chrome.com/docs/android/custom-tabs/
- Gradle: https://gradle.org/

---

**Last updated:** April 2026
