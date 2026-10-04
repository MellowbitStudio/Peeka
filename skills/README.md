# Peeka agent skill

This folder publishes the **`peeka`** skill for installing and using Mellowbit Studio's macOS Quick Look app. It covers App Store setup, features and supported formats, Free and Pro, preview switches, and troubleshooting.

The skill uses the portable `SKILL.md` format with bundled references. Codex, Claude Code, and other agents supported by the [Skills CLI](https://github.com/vercel-labs/skills) can install it. It provides instructions and product knowledge; performing desktop actions requires the agent's own local tools. The Peeka app requires **macOS 14 or later**.

## Install from GitHub

After these files are published to the repository's default branch:

```sh
npx skills add MellowbitStudio/Peeka --skill peeka
```

The interactive installer lets you select agents. To target Codex and Claude Code explicitly:

```sh
npx skills add MellowbitStudio/Peeka --skill peeka --agent codex claude-code
```

Add `--global` to make the skill available across projects instead of only the current project:

```sh
npx skills add MellowbitStudio/Peeka --skill peeka --agent codex claude-code --global
```

Use `--list` to inspect published skills without installing:

```sh
npx skills add MellowbitStudio/Peeka --list
```

These commands install the **agent skill**. To download the **Peeka app**, follow the [Mac App Store listing](https://apps.apple.com/app/peeka-ultimate-quicklook-app/id6813012289) and the skill's setup instructions. No npm package or hosted service for Peeka is required.

## Try local changes

From the repository root, discover or install the local skill before publishing:

```sh
npx skills add ./skills --list
npx skills add ./skills --skill peeka --agent codex claude-code
```

Installation requires a Node.js/npm environment capable of running `npx skills`. The Skills CLI handles each agent's installation location; keep the distributable source in `skills/peeka/`.

## Example requests

- “Use the Peeka skill to install the app from the Mac App Store and set up Finder previews.”
- “Can Peeka preview an XAPK? Is Pro required?”
- “Turn off Peeka's Markdown previews and keep source-code previews enabled.”
- “My `.ts` file still shows a different preview. Help me diagnose it.”
- “Peeka Pro was purchased before. Help me restore it.”
- “使用 Peeka skill，帮我开启 JSON 文件预览。”

Invoke `$peeka` in agents that support that syntax; other agents can load it through their skill mechanism. Responses follow the user's language. Apple Account authentication and purchase confirmation remain with the user.

## Contents and maintenance

```text
skills/
├── README.md
└── peeka/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
        ├── install-and-controls.md
        ├── features-and-plans.md
        └── troubleshooting.md
```

`agents/openai.yaml` supplies optional Codex UI metadata; the portable instructions are in `SKILL.md` and `references/`. Those references travel with the installed skill and work without this repository checkout.

Update the bundled facts and review date when Peeka's public capabilities change. Keep both root READMEs consistent with the skill, use the app's StoreKit price rather than a fixed amount, and verify changed settings labels against the installed macOS/app version. The app's source code is not included in this public repository.
