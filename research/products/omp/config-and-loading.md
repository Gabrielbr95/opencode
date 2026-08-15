# OMP Config and Loading

## Freshness
- Last verified: 2026-08-06
- Verified against:
  - OMP `README.md`
  - OMP `docs/config-usage.md`
  - OMP `docs/settings.md`
  - OMP `docs/context-files.md`
  - OMP `docs/models.md`
  - OMP `docs/providers.md`
  - OMP `docs/mcp-config.md`
  - OMP `docs/memory.md`
  - OMP `docs/extensions.md`
  - OMP `docs/extension-loading.md`
  - OMP `docs/skills.md`
  - OMP `docs/system-prompt-customization.md`
  - OMP `docs/approval-mode.md`
  - OMP `docs/hooks.md`
  - OMP `docs/session-operations-export-share-fork-resume.md`
  - OMP `docs/environment-variables.md`
- Product version: current docs snapshot; exact installed local version not verified
- Stability: Low
- Recheck triggers:
  - config root or precedence docs change
  - settings schema changes materially
  - MCP/config translation behavior changes materially
  - model/provider config docs change materially

## Scope
- documented OMP configuration file names, locations, and formats
- documented settings, overlay, and precedence behavior
- documented context, system-prompt, skill, MCP, extension, memory, and model-loading surfaces
- documented gaps where the current official docs do not specify a universal behavior

## Canonical Boundary
This note records product-specific configuration and loading facts for OMP.

It does not own:
- feature comparisons against Pi or opencode
- trust interpretation beyond directly documented config/approval behavior
- migration recommendations

## Documented Config Roots, File Names, and Formats

### Native OMP roots
- user root: `~/.omp/agent/...`
- project root: `<cwd>/.omp/...`
- named profiles relocate the native user root to `~/.omp/profiles/<name>/agent/...`
- profile selection is documented via:
  - `omp --profile <name>`
  - `OMP_PROFILE`
  - legacy `PI_PROFILE`

### Generic source priority
`docs/config-usage.md` documents this source priority for generic config discovery:
1. `.omp`
2. `.claude`
3. `.codex`
4. `.gemini`

### Settings files
- global settings:
  - `~/.omp/agent/config.yml`
  - existing `~/.omp/agent/config.yaml` is also read and updated in place
  - legacy `~/.omp/agent/settings.json`
- project settings:
  - `<cwd>/.omp/config.yml`
  - legacy `<cwd>/.omp/settings.json`

### Model config files
- `~/.omp/agent/models.yml`
- `~/.omp/agent/models.yaml`
- legacy `~/.omp/agent/models.json`

### Native context and rule files
- `~/.omp/agent/AGENTS.md`
- `~/.omp/agent/RULES.md`
- `<nearest-non-empty-ancestor>/.omp/AGENTS.md`
- `<nearest-non-empty-ancestor>/.omp/RULES.md`

### System-prompt customization files
- `SYSTEM.md`
- `APPEND_SYSTEM.md`
- `TITLE_SYSTEM.md`
- docs state these are searched under project bases first, then user bases for:
  - `.omp`
  - `.claude`
  - `.codex`
  - `.gemini`

### MCP files
- preferred native files:
  - `.omp/mcp.json`
  - `~/.omp/agent/mcp.json`
- native compatibility files:
  - `.omp/.mcp.json`
  - `~/.omp/agent/.mcp.json`
- fallback root files:
  - `mcp.json`
  - `.mcp.json`

### Formats
- settings are documented as YAML mappings
- the generic config loader supports:
  - `.yml`
  - `.yaml`
  - `.json`
  - `.jsonc`
- settings YAML top-level must be a mapping

## Documented Settings Resolution and Merge Behavior

### Effective precedence
`docs/config-usage.md` documents effective settings precedence as:
- `defaults <- global <- project <- PI_CONFIG_FILES overlays <- --config overlays <- runtime overrides`

### Overlay sources
- `PI_CONFIG_FILES` is a platform path-list of overlay files
- repeated `--config <file>` overlays load after `PI_CONFIG_FILES`
- later overlay files override earlier overlay files

### Merge rules
`docs/settings.md` documents:
- objects are deep-merged
- scalars are replaced
- arrays are replaced wholesale

### Global write behavior
`docs/settings.md` documents that:
- `/settings`, `omp config set`, and `omp config reset` write to the global main YAML file
- project settings and config overlays are read-only from the settings API except for project-scoped model role storage behavior

### Project-scoped role storage
`docs/settings.md` documents:
- `modelRoleStorage` values:
  - `global`
  - `project`
- with `modelRoleStorage: project`, model-selector role assignments update only `modelRoles` in `<cwd>/.omp/config.yml`

### Path-scoped array entries
`docs/settings.md` documents path-scoped entries for:
- `enabledModels`
- `disabledProviders`

Accepted path keys:
- `path`
- `paths`
- `pathPrefix`
- `pathPrefixes`

Accepted value keys:
- `models` for `enabledModels`
- `providers` for `disabledProviders`
- `values` or `items` for either setting

## Documented Discovery and Dedup Behavior

### Generic helper ordering
`docs/config-usage.md` states that generic helpers return:
- user-level entries first
- then project-level entries

### Capability dedup behavior
`docs/config-usage.md` documents keyed first-wins behavior for capability items with the same key.

Documented keyed capability examples:
- skills: `name`
- tools: `name`
- hooks: `${type}:${tool}:${name}`
- extension modules: `name`
- extensions: `name`

The same doc states that settings capability items are not deduplicated.

### Settings-specific provider caveat
`docs/config-usage.md` documents that:
- project settings are deep-merged in returned order
- lower-priority provider settings can override higher-priority settings because settings capability items are not deduplicated
- native `.omp/config.yml` `modelRoles` are then reapplied as the authoritative project model-role layer

## Documented Context, Rules, and Instruction Loading

### Native context and rules
`docs/context-files.md` and `docs/config-usage.md` document native files:
- `~/.omp/agent/AGENTS.md`
- `~/.omp/agent/RULES.md`
- nearest non-empty ancestor `.omp/AGENTS.md`
- nearest non-empty ancestor `.omp/RULES.md`

### Other supported context conventions
`docs/context-files.md` documents support for:
- `~/.claude/CLAUDE.md`
- `<cwd>/.claude/CLAUDE.md`
- `~/.codex/AGENTS.md`
- `~/.gemini/GEMINI.md`
- `<cwd>/.gemini/GEMINI.md`
- `~/.config/opencode/AGENTS.md`
- `~/.copilot/copilot-instructions.md`
- `<cwd>/.github/copilot-instructions.md`
- `.agent/AGENTS.md`
- `.agents/AGENTS.md`
- standalone `AGENTS.md`
- `.github/instructions/**/*.instructions.md`

### Documented context-provider priorities
`docs/context-files.md` documents these provider priorities:
- `native` 100
- `claude` 80
- `agents`, `codex` 70
- `gemini` 60
- `opencode` 55
- `github` 30
- `agents-md` 10

### Documented shadowing and injection rules
`docs/context-files.md` documents:
- one user context file survives across providers
- one project context file survives per directory depth
- at the same depth, higher-priority provider shadows lower-priority provider
- across depths, multiple files can survive
- final injection order is farther ancestors first, then closer project files, then the user file

### `RULES.md`
`docs/context-files.md` and `docs/config-usage.md` document that:
- `RULES.md` is loaded as an always-apply sticky rule
- it is read only from native locations
- it is always sticky; frontmatter cannot make it non-sticky
- both top-level candidates are synthesized with rule name `RULES`
- rule dedup is name-based
- the docs state that in the usual case, user `RULES.md` shadows project `RULES.md`

### `@` imports in context files
`docs/context-files.md` documents:
- `@path` expands inline before injection
- relative paths resolve from the importing file's directory
- `~/` and `~` resolve from home
- imports inside fenced code blocks and inline code are not expanded
- `git@...` and email-like tokens are not treated as imports
- trailing punctuation is trimmed
- recursion limit is 5 hops
- cycles are skipped
- missing or unreadable targets leave the literal `@token` unchanged

## Documented System Prompt Customization

### File roles
`docs/system-prompt-customization.md` documents:
- `SYSTEM.md` switches to the bundled custom-system-prompt template
- `APPEND_SYSTEM.md` appends text to the rendered prompt
- `TITLE_SYSTEM.md` customizes automatic session title generation only

### Discovery behavior
`docs/system-prompt-customization.md` and `docs/config-usage.md` document:
- search order is project-first, then user-level
- bases searched at each scope are:
  - `.omp`
  - `.claude`
  - `.codex`
  - `.gemini`
- discovery for these files does not walk ancestors

### CLI flags with higher precedence
- `--system-prompt <text-or-file>`
- `--append-system-prompt <text-or-file>`

## Documented Model and Provider Configuration

### Primary files and root shape
`docs/models.md` documents:
- primary files:
  - `~/.omp/agent/models.yml`
  - `~/.omp/agent/models.yaml`
- root key: `providers`
- unknown root keys fail schema validation

### Provider-level keys documented in `docs/models.md`
- `baseUrl`
- `apiKey`
- `api`
- `headers`
- `authHeader`
- `auth`
- `disableStrictTools`
- `discovery`
- `modelOverrides`
- `models`
- `transport`
- `remoteCompaction`
- `compat`

### Model-level keys documented in `docs/models.md`
- `id`
- `name`
- `api`
- `reasoning`
- `input`
- `cost.input`
- `cost.output`
- `cost.cacheRead`
- `cost.cacheWrite`
- `contextWindow`
- `maxTokens`
- `headers`
- `compat`
- `contextPromotionTarget`
- `compactionModel`
- `remoteCompaction`

### Allowed `api` values documented in `docs/models.md`
- `openai-completions`
- `openai-responses`
- `openai-codex-responses`
- `azure-openai-responses`
- `anthropic-messages`
- `bedrock-converse-stream`
- `google-generative-ai`
- `google-gemini-cli`
- `google-vertex`

### Allowed `auth` values documented in `docs/models.md`
- `apiKey`
- `none`
- `oauth`

### Allowed `discovery.type` values documented in `docs/models.md`
- `ollama`
- `llama.cpp`
- `lm-studio`
- `openai-models-list`
- `proxy`
- `litellm`

### Model-role keys documented in `docs/settings.md`
- `modelRoles`
- documented built-in roles:
  - `default`
  - `smol`
  - `slow`
  - `vision`
  - `plan`
  - `designer`
  - `commit`
  - `tiny`
  - `task`
  - `advisor`
- related keys:
  - `modelRoleStorage`
  - `modelProviderOrder`
  - `cycleOrder`
  - `enabledModels`
  - `disabledProviders`

### Provider availability and credential resolution
`docs/models.md` documents that a provider or model is available only if:
1. provider id is not in effective `disabledProviders`
2. provider is keyless or credentials resolve

`docs/models.md` documents credential resolution order as:
1. runtime override, such as `--api-key`
2. `models.yml` provider `apiKey`
3. stored OAuth credential
4. login-sourced stored API key
5. provider environment variable
6. other stored API key
7. `models.yml` fallback resolver

### `.env` precedence
`docs/providers.md` documents this order:
1. inherited process environment
2. `<cwd>/.env`
3. `~/.omp/agent/.env`
4. `~/.omp/.env`
5. `~/.env`

## Documented Tool Approval and Related Policy Surfaces

### Settings keys
`docs/approval-mode.md` and `docs/settings.md` document:
- `tools.approvalMode`
- `tools.approval.<toolName>`

### `tools.approvalMode` values
- `always-ask`
- `write`
- `yolo`

`docs/approval-mode.md` documents `yolo` as the default.

### Per-tool policy values
- `allow`
- `deny`
- `prompt`

### Tool approval tiers
`docs/approval-mode.md` documents:
- `read`
- `write`
- `exec`

The same doc states:
- tools without an `approval` declaration are treated as `exec`
- MCP server tools declare `write`
- `--auto-approve` and `--yolo` force `tools.approvalMode: yolo` for the session
- for the `computer` tool, `read_only: true` maps to `read`; missing, malformed, or `false` maps to `exec`
- subagents run headless with `tools.approvalMode: yolo`; user `tools.approval.<tool>` still applies

### Bash-related policy keys
`docs/settings.md` documents:
- `bash.patterns[].match`
- `bash.patterns[].approval`
- `bashInterceptor.enabled`
- `bashInterceptor.patterns[].pattern`
- `bashInterceptor.patterns[].tool`
- `bashInterceptor.patterns[].message`

## Documented Skills Surfaces

### Required layout
`docs/skills.md` documents:
- `<skills-root>/<skill-name>/SKILL.md`

### Documented frontmatter keys
- `name`
- `description`
- `globs`
- `alwaysApply`
- `hide`
- `disableModelInvocation`
- kebab-case `disable-model-invocation` is normalized

### Discovery and toggles
`docs/skills.md` documents:
- native provider loads skills from ancestor `.omp/skills` directories plus `~/.omp/agent/skills`
- `skills.customDirectories` scans non-recursively with the same `*/SKILL.md` layout
- managed skills provider id is `omp-managed`; it is loaded dead-last
- custom-directory skills override same-named default provider skills
- duplicate custom-directory names remain first-wins

Documented settings and filters:
- `skills.enabled`
- `skills.enableSkillCommands`
- `skills.customDirectories`
- `enableCodexUser`
- `enableClaudeUser`
- `enableClaudeProject`
- `enablePiUser`
- `enablePiProject`
- `enableAgentsUser`
- `enableAgentsProject`
- `ignoredSkills`
- `includeSkills`
- `disabledExtensions` entries of form `skill:<name>`

### Skill URL scheme
`docs/skills.md` documents:
- `skill://<name>`
- `skill://<name>/<relative-path>`

## Documented MCP Surfaces

### Schema reference
`docs/mcp-config.md` documents:
- `$schema: "https://raw.githubusercontent.com/can1357/oh-my-pi/main/packages/coding-agent/src/config/mcp-schema.json"`

### Top-level keys
`docs/mcp-config.md` documents:
- `$schema`
- `mcpServers`
- `disabledServers`
- `enabledServers`

### Per-server shared keys
`docs/mcp-config.md` documents:
- `enabled`
- `timeout`
- `requestIdFormat`
- `auth`
- `oauth`

### Transport-specific keys
`docs/mcp-config.md` documents:
- stdio:
  - `type` omitted or `"stdio"`
  - `command`
  - `args`
  - `env`
  - `cwd`
- http:
  - `type: "http"`
  - `url`
  - `headers`
- sse:
  - `type: "sse"`
  - `url`
  - `headers`

### Auth blocks
`docs/mcp-config.md` documents:
- `auth.type`
- `auth.credentialId`
- `auth.tokenUrl`
- `auth.clientId`
- `auth.clientSecret`
- `auth.resource`
- `oauth.clientId`
- `oauth.clientSecret`
- `oauth.redirectUri`
- `oauth.callbackPort`
- `oauth.callbackPath`
- `oauth.prompt`

### Discovery and dedup behavior
`docs/mcp-config.md` documents this provider order:
1. OMP native config
2. OMP extension packages
3. Claude Code
4. Claude marketplace plugins and Codex
5. Gemini CLI
6. OpenCode
7. Cursor and Windsurf
8. VS Code
9. root `mcp.json` / `.mcp.json`

The same doc states:
- first definition wins
- duplicate names are not merged
- a different name is also shadowed if transport, endpoint or command inputs, auth, and request-id mode are equivalent to a higher-priority definition

### Imported MCP config files documented in `docs/mcp-config.md`
- Claude Code:
  - `~/.claude.json`
  - `~/.claude/mcp.json`
  - `.claude/.mcp.json`
  - `.claude/mcp.json`
- Codex:
  - `~/.codex/config.toml`
  - `.codex/config.toml`
  - section `[mcp_servers.*]`
- Gemini CLI:
  - `~/.gemini/settings.json`
  - `.gemini/settings.json`
- OpenCode:
  - `~/.config/opencode/opencode.json`
  - project-root `opencode.json`
- Cursor:
  - `~/.cursor/mcp.json`
  - `.cursor/mcp.json`
- Windsurf:
  - `~/.codeium/windsurf/mcp_config.json`
  - `.windsurf/mcp_config.json`
- VS Code:
  - `.vscode/mcp.json` using `mcp.servers`

### Extra MCP controls
`docs/mcp-config.md` documents:
- `OMP_MCP_TIMEOUT_MS` overrides per-server `timeout`
- `mcp.enableProjectConfig: false` excludes every project-level MCP source before deduplication

## Documented Extensions, Hooks, and Tool Loading

### Extension directories and settings
`docs/extensions.md` and `docs/extension-loading.md` document native extension module roots:
- `<cwd>/.omp/extensions`
- active agent directory `extensions/`

Legacy JSON extension lists documented:
- `<cwd>/.omp/settings.json#extensions`
- active agent directory `settings.json#extensions`

Documented settings keys:
- `extensions`
- `disabledExtensions`

### Package manifest keys
`docs/extensions.md` documents:
- `package.json` key `omp.extensions`
- legacy `pi.extensions`

### Documented extension load order
`docs/extensions.md` documents:
1. native auto-discovered modules
2. discovered JS or TS hook factories
3. installed plugin extension entries
4. explicit configured paths

### CLI controls
- `--no-extensions`
- `--extension` / `-e`
- `--hook` is documented as an alias for `--extension`

### Explicit file support
`docs/extensions.md` and `docs/extension-loading.md` document:
- explicit files may be:
  - `.ts`
  - `.js`
  - `.mjs`
  - `.cjs`
- auto-scanned native and configured directories discover `.ts` and `.js`
- directory manifest entry resolution can also recognize `index.mjs` and `index.cjs`

### Disable-id format
`docs/extensions.md` documents `disabledExtensions` entries for extension modules in the form:
- `extension-module:<derivedName>`

### Hook paths
`docs/hooks.md` and `docs/config-usage.md` document:
- `hooks/pre/*`
- `hooks/post/*`

### Hooks runtime status
`docs/extensions.md` and `docs/hooks.md` document:
- default runtime uses the extension runner path
- JS or TS hook factories discovered via hook capability are loaded as extension modules

### Custom tool paths
`docs/config-usage.md` documents:
- `tools/*.{json,md,ts,js,sh,bash,py}`
- `tools/<name>/index.ts`

## Documented Memory and Session-Related Config Surfaces

### Memory keys
`docs/memory.md` documents:
- `memory.backend` with values:
  - `off`
  - `local`
  - `hindsight`
  - `mnemopi`
- `autolearn.enabled`
- `memories.maxRolloutAgeDays`
- `memories.minRolloutIdleHours`
- `memories.maxRolloutsPerStartup`
- `memories.threadScanLimit`
- `memories.maxRawMemoriesForGlobal`
- `memories.stage1Concurrency`
- `memories.stage1LeaseSeconds`
- `memories.stage1RetryDelaySeconds`
- `memories.phase2LeaseSeconds`
- `memories.phase2RetryDelaySeconds`
- `memories.phase2HeartbeatSeconds`
- `memories.rolloutPayloadPercent`
- `memories.phase1InputTokenLimit`
- `memories.fallbackTokenLimit`
- `memories.summaryInjectionTokenLimit`

### Hindsight keys
`docs/memory.md` documents:
- `hindsight.apiUrl`
- `hindsight.apiToken`
- `hindsight.bankId`
- `hindsight.autoRecall`

### Memory-related URLs
`docs/memory.md` documents:
- `memory://root`
- `memory://root/MEMORY.md`
- `memory://root/learned.md`
- `memory://root/skills/<name>/SKILL.md`

### Session-related config surfaces directly documented
- `modelRoleStorage` in `docs/settings.md`
- `autoResume` is referenced in `docs/session-operations-export-share-fork-resume.md`
- `TITLE_SYSTEM.md` controls automatic session titles
- `modelRoles.tiny` is documented in `docs/settings.md` as the role used for lightweight background tasks including titles and memory-related work

## Documented Gaps and Unspecified Areas

### No single universal non-settings merge rule documented
The official docs document subsystem-specific behavior for:
- settings
- context files
- skills
- MCP
- extensions

The same docs do not document a single universal merge rule for all non-settings capability content.

### Session-operation configuration surface is only partially documented
The official docs document session export, share, fork, resume, fresh, and related actions mainly as commands or CLI behavior. In the current docs set, only a smaller related settings surface is explicitly documented, including:
- `autoResume`
- `modelRoleStorage`
- `TITLE_SYSTEM.md`

### MCP schema/runtime mismatch noted in docs
`docs/mcp-config.md` states that:
- the runtime and config writer accept `:` in server names
- the bundled JSON schema pattern currently omits `:`

### Third-party MCP translation does not expose every OMP-native field
`docs/mcp-config.md` states that `requestIdFormat` is only read from:
- OMP-native MCP files
- root `mcp.json` / `.mcp.json`
- OMP extension packages

The same doc states that translated third-party MCP configs ignore that field.

## References
- [OMP README](https://raw.githubusercontent.com/can1357/oh-my-pi/main/README.md)
- [Configuration discovery and resolution](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/config-usage.md)
- [Settings](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/settings.md)
- [Context files](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/context-files.md)
- [Models](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/models.md)
- [Providers](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/providers.md)
- [MCP configuration](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/mcp-config.md)
- [Memory](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/memory.md)
- [Extensions](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/extensions.md)
- [Extension loading](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/extension-loading.md)
- [Skills](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/skills.md)
- [System prompt customization](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/system-prompt-customization.md)
- [Approval mode](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/approval-mode.md)
- [Hooks](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/hooks.md)
- [Session operations](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/session-operations-export-share-fork-resume.md)
- [Environment variables](https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/environment-variables.md)
