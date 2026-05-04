package com.ground.moral;

import android.content.ComponentName;
import android.net.Uri;
import android.os.Bundle;

import androidx.activity.ComponentActivity;
import androidx.browser.customtabs.CustomTabsClient;
import androidx.browser.customtabs.CustomTabsIntent;
import androidx.browser.customtabs.CustomTabsServiceConnection;
import androidx.browser.customtabs.CustomTabsSession;
import androidx.browser.trusted.TrustedWebActivityIntentBuilder;

/**
 * Launcher activity that opens the Ground PWA in a Trusted Web Activity.
 * TWA gives full-screen, no-browser-chrome experience — looks native.
 *
 * If TWA verification fails (no matching assetlinks.json), it falls back
 * to a Custom Chrome Tab (functional, just shows a minimal browser bar).
 */
public class LauncherActivity extends ComponentActivity {

    private static final Uri DEFAULT_URI =
            Uri.parse("https://ground-moral.onrender.com");

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Try to launch as TWA via Custom Tabs
        String packageName = CustomTabsClient.getPackageName(this, null);

        if (packageName != null) {
            // Chrome (or another Custom Tabs provider) is available
            CustomTabsClient.bindCustomTabsService(this, packageName,
                    new CustomTabsServiceConnection() {
                        @Override
                        public void onCustomTabsServiceConnected(
                                ComponentName name, CustomTabsClient client) {
                            // Warm up for faster load
                            client.warmup(0);
                            CustomTabsSession session = client.newSession(null);

                            if (session != null) {
                                // Launch as Trusted Web Activity
                                TrustedWebActivityIntentBuilder builder =
                                        new TrustedWebActivityIntentBuilder(DEFAULT_URI);
                                builder.build(session)
                                       .launchTrustedWebActivity(LauncherActivity.this);
                            } else {
                                // Fallback: Custom Tab
                                launchCustomTab();
                            }
                            finish();
                        }

                        @Override
                        public void onServiceDisconnected(ComponentName name) {
                            // No-op
                        }
                    });
        } else {
            // No Custom Tabs provider — fall back to regular Custom Tab intent
            launchCustomTab();
            finish();
        }
    }

    private void launchCustomTab() {
        CustomTabsIntent intent = new CustomTabsIntent.Builder()
                .setShowTitle(false)
                .build();
        intent.launchUrl(this, DEFAULT_URI);
    }
}
