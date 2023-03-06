
# CI

For configuring Continuous Integration for this Python Application using GitHub Actions.

The "python-app.yml" [configuration file](/.github/workflows/python-app.yml) specifies what steps should take place during the CI build.



In GitHub repository settings, find the secrets and variables menu for "actions", and add a "New repository secret" called `GOOGLE_API_CREDENTIALS`, and paste the JSON content from the "google-credentials.json" file.
