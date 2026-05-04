# Ground TWA Quick Start

## Build & Test (5 minutes)

```bash
# Debug build for testing
./gradlew assembleDebug

# Install on device
./gradlew installDebug

# Output: app/build/outputs/apk/debug/app-debug.apk
```

## One-time Keystore Setup

```bash
# Generate a keystore (save the password!)
keytool -genkey -v -keystore ground-keystore.jks \
  -keyalg RSA -keysize 2048 -validity 10000 -alias ground-key

# Copy gradle.properties.example to gradle.properties
cp gradle.properties.example gradle.properties

# Edit gradle.properties with your keystore path and password
nano gradle.properties
```

## Release Build

```bash
# Build release APK (requires gradle.properties with keystore config)
./gradlew assembleRelease

# Output: app/build/outputs/apk/release/app-release.apk
```

## Digital Asset Links (for fullscreen TWA)

1. Get your keystore fingerprint:
   ```bash
   keytool -list -v -keystore ground-keystore.jks -alias ground-key
   # Copy the SHA256 line
   ```

2. Create `.well-known/assetlinks.json` on your web server:
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

3. Test it works:
   ```bash
   curl https://ground-moral.onrender.com/.well-known/assetlinks.json
   ```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Build fails | Install Java 11+: `java -version` |
| APK won't install | `./gradlew installDebug -x lint` |
| TWA shows browser bar | assetlinks.json not found or SHA256 mismatch |
| Gradle not found | Run from android-twa directory |

## Security Notes

- Never commit `gradle.properties` (contains passwords)
- Keep `ground-keystore.jks` private and backed up
- Store keystore password securely
- Do not share keystore files

## Further Reading

- Full guide: `../DEPLOY.md`
- Android docs: https://developer.chrome.com/docs/android/trusted-web-activity/
