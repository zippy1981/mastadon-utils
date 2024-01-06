# Mastadon utils

Some mastadon utilities I wrote

## Latest build statuses

| Workflow | Status |
|---|:---|
| Lint README.md | ![Lint README.md status badge](https://github.com/USERNAME/REPOSITORY/actions/workflows/readme.yml/badge.svg) |

## configuration

To run the script you will need a `.secrets.toml` fie with the API Key like so:

```toml
dynaconf_merge = true # very important to not overwrite settings.toml

[MASTODON_API]
KEY="YOUR_API_KEY"
```

Also set the server in `settings.toml`.
