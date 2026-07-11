# Security Policy

## Scope

This repository contains a content catalog (Markdown files, JSON schemas) and tooling scripts (Python). It does not run as a hosted service and does not handle user data, authentication, or network requests in production.

Security concerns most likely to be relevant:

- Malicious content embedded in taxonomy entries that could affect downstream consumers
- Vulnerabilities in the `tools/` Python scripts (e.g., path traversal, code injection)
- Dependency vulnerabilities in `requirements-dev.txt` or `package.json`

## Reporting a Vulnerability

If you discover a security issue, please do not open a public GitHub issue. Instead, report it privately through GitHub's vulnerability reporting for this repository: open the **Security** tab and choose **Report a vulnerability** (direct link: <https://github.com/product-on-purpose/writing-style-catalog/security/advisories/new>). Include:

1. A description of the vulnerability and its potential impact
2. Steps to reproduce
3. Any relevant file paths or code locations

The maintainer will acknowledge receipt in the advisory thread within 72 hours and provide a timeline for resolution. Confirmed vulnerabilities will be patched and disclosed in the CHANGELOG with appropriate credit to the reporter.

## Supported Versions

Only the latest release on the `main` branch is actively maintained. Older tags are provided as historical reference only.
