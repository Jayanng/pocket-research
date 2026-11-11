# Shipping AI Agents in 2026: The Seven-Service Security Pipeline Hiding in Plain Sight on Pocket

> Quest: **Create an Industry-Specific Pocket Use Case**. Industry: AI agent development. All claims verified November 11, 2026.

## The problem: agents became an attack surface faster than anyone shipped defenses

The incident record shows how fast agents became an attack surface. A curated database counts **55 notable AI-agent security incidents between May 2025 and September 2026**, prompt injection the largest class at **47%** (host0, 2026). NVD entries mentioning prompt injection, MCP or AI agents rose from **13 in Q2 2025 to 256 in Q3 2026**, 182 touching MCP. Unit 42 reports injection is now "actively weaponized" on the web. The LiteLLM 1.107.0 compromise (Microsoft, October 2026) turned a popular AI gateway package into a credential collector and landed on CISA's exploited list; the Miasma worm used agent config files to disable 73 Microsoft GitHub repositories; and the Cloud Security Alliance's confused-deputy analysis traces a GitHub issue title to a rogue npm release. Every team shipping agents faces one question: **what can my agent safely read, depend on, and talk to?**

## The matching services: a seven-service security pipeline

The portal's security category maps onto that question almost one-to-one. All seven services below are live today, $0.005 per call, no account and no API key:

| Stage | Service | Answers |
|---|---|---|
| Screen untrusted input | [`prompt-injection-detect`](https://agent.pocket.network/services/prompt-injection-detect) | safe / suspicious / malicious verdict on agent-bound text |
| Screen untrusted input | [`url-phishing-reputation`](https://agent.pocket.network/services/url-phishing-reputation) | phishing verdict without fetching — never "clean," only suspicious or unknown |
| Protect data in transit | [`pii-redaction`](https://agent.pocket.network/services/pii-redaction) | mask names, SSNs, emails, phones before third-party calls or logs |
| Screen dependencies | [`package-advisories`](https://agent.pocket.network/services/package-advisories) | vulnerabilities across seven ecosystems via deps.dev and OSV |
| Screen dependencies | [`taint-check`](https://agent.pocket.network/services/taint-check) | lockfile scan for vulnerable *and confirmed-malicious* packages |
| Screen counterparties | [`agent-trust`](https://agent.pocket.network/services/agent-trust) | RDAP/DNS, live TLS, sanctions and EVM checks before trusting a counterparty |
| Screen impersonation | [`brand-protection`](https://agent.pocket.network/services/brand-protection) | lookalike domains: typos, homoglyphs, TLD swaps, with registry and TLS evidence |

A concrete workflow: route external input through `prompt-injection-detect` before the model sees it, redact PII before third-party calls, gate dependency changes on `package-advisories` and `taint-check` in CI, and run `agent-trust` plus `brand-protection` before the agent touches a new domain. Each gate is one call at $0.005 and deterministic on identical input — a gate that answers differently on retry is one you cannot write policy against.

```
untrusted text ──► prompt-injection-detect ──► pii-redaction ──► model
new dependency ──► package-advisories ──► taint-check ──► CI gate
new counterparty ─► agent-trust ──► brand-protection ──► allow contact
```

## Limitations, stated honestly

These are deterministic, rule-based checks, not trained ML classifiers — a feature for auditability, a limit for recall. The phishing service deliberately never returns "clean," only "suspicious or unknown." Threat intelligence may lag by a cache cycle. None of it replaces the structural fixes the record demands: least privilege, human confirmation for destructive actions, sandboxing. This is the screening layer; the architecture is still the builder's.

## Why this use case is real

The pain is documented by Microsoft, Unit 42, the Cloud Security Alliance and CISA, all within the last twelve months and all independent of Pocket. The matching services are live and priced for automation. The gap between "agents are under attack" and "here is a callable pipeline for it" is exactly where a developer need lives.

## References

1. [agent.pocket.network/services.json](https://agent.pocket.network/services.json), checked November 11, 2026: seven services, $0.005/call.
2. [host0, State of AI Agent Security 2026](https://host0.ai/blog/state-of-ai-agent-security-2026), stats verified November 11, 2026.
3. [Microsoft Security Blog, LiteLLM 1.107.0 supply chain compromise](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/), October 23, 2026.
4. [CSA, Confused Deputy Attacks on Autonomous AI Agents](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-agent-confused-deputy-prompt-injection/), 2026.
5. [CSA, AI Coding Agents as Attack Surface](https://labs.cloudsecurityalliance.org/research/ai-coding-agent-attack-surface-mcp-repository-poisoning-v1-0/), 2026.

---

*Authored by [@Jayanng](https://github.com/Jayanng), who also filed [poktroll issue #2037](https://github.com/pokt-network/poktroll/issues/2037), a ring-construction bug in the Pocket protocol, November 2026.*
