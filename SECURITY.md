# Security Policy

## Supported Versions

This project follows the release scheme `vMAJOR.CODE.RESOURCE`.

| Version Line | Security Updates |
| --- | --- |
| `main` | Yes |
| `v1.x.x` | Yes |
| `v0.x` and older | No |

Only the latest `main` branch and current major release line receive active security fixes.

## Reporting a Vulnerability

### Preferred (Private)

Use GitHub private vulnerability reporting:

- [Report a vulnerability](https://github.com/Musawer1214/pashto-language-resources/security/advisories/new)

Do not open a public issue with exploit details.

### If Private Reporting Is Not Available

Open a minimal public issue with title `Security Report Request` and no technical details. A maintainer will move follow-up to a safer channel.

## What To Include

Please include:

- Affected file, component, or script
- Reproduction steps and impact
- Proof of concept (if safe)
- Suggested fix (if available)
- Whether the issue is already public

## Response Timeline

- Acknowledgment: within 72 hours
- Initial triage: within 7 days
- Remediation target:
  - Critical: 14 days
  - High: 30 days
  - Medium/Low: next scheduled maintenance release

If timelines change, maintainers will provide updates in the advisory thread.

## Disclosure Policy

- Please use coordinated disclosure.
- Do not publish exploit details until a fix or mitigation is released.
- After release, maintainers may publish a security advisory and changelog note.

## Scope Notes

In scope:

- Repository code and automation scripts
- GitHub Actions workflows in this repository
- Published search page code under `docs/search/`

Out of scope:

- Vulnerabilities only in third-party platforms/services not controlled by this repository
- Social engineering and physical access attacks
