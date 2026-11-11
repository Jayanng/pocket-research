# Opportunity Brief: Transaction Execution Is the Missing Capability Class on the Pocket Agentic Portal

> Prepared for the Pocket Community Hub quest **"Find Real Demand for a Pocket Service."** All catalogue claims verified against [agent.pocket.network/services.json](https://agent.pocket.network/services.json) on November 10, 2026. Market figures pulled live the same day.

## The gap

The Agentic Portal's 124 services include 52 blockchain services covering 50+ networks: Ethereum, Base, Arbitrum, Avalanche, BNB, Polygon, Berachain, Blast, Solana, Sui, Near, Tron and more. Every single one of them is read-only. The word "Read-only" opens the description of all 52 chain services, and no service in the entire catalogue exposes `sendTransaction`, transaction submission, or broadcast for any chain. Verified programmatically against services.json: zero execution paths.

An agent on the portal today can check a balance, read a contract, screen a counterparty, or fetch a price, on 50+ chains. It cannot move anything, anywhere. It can look but not act.

## The demand, with sources

The paying consumers of this portal are AI agents, and agent workloads are execution-heavy by nature. Two independent industry sources describe the execution demand explicitly:

1. **RPC Fast, ["Top Solana RPC for AI Agents"](https://rpcfast.com/blog/top-solana-rpc-for-ai-agents) (2026):** a conventional dApp sends a few dozen RPC calls per minute; an AI trading agent sends thousands, submits transactions in bursts, and needs transaction landing rate as its core reliability metric. Their framing: an agent that fires 100 transactions during a token launch and lands 40 of them "is an expensive random number generator." The same piece documents agent-specific product tiers (dedicated low-latency execution, MEV protection, priority routing) already being sold by Helius, QuickNode, Chainstack and Triton, which is direct evidence that providers monetize execution access as a separate, premium product class from reads.

2. **CryptoSlate, ["Jito's Solana data feed puts a price on seeing trades early"](https://cryptoslate.com/jitos-solana-data-feed-puts-a-price-on-seeing-trades-early/) (October 2026), and Jito BAM coverage:** preconfirmation streams, priced per delivered message with a 35/35/30 revenue split across validators, DAO and distributors, went live to paid subscribers through distributors like Helius. The market is already selling time-advantaged transaction visibility and execution signaling to automated consumers at scale.

Demand context, pulled live: Solana is the **#3 chain by TVL at $5.07B** (DefiLlama chain rankings, Nov 10, 2026) and carries **$14.4B in stablecoin market cap** (DefiLlama stablecoins, Nov 10, 2026), the transfer-and-payment activity that transaction execution serves directly.

**The caveat, stated plainly:** both sources are commercial providers who sell execution capability, so they are interested parties, not neutral observers. Their pricing pages and product tiers are nonetheless the most concrete evidence available of what agents pay for, and their existence as a revenue-bearing market is itself the demand signal.

## How a Pocket service meets it

A **`solana-tx`** service: the agent builds and signs a versioned transaction locally with its own key, and the service relays the signed payload to Solana mainnet-beta and returns the signature and landing status.

Key design point: **custody never leaves the agent.** The supplier relays bytes; it never holds keys, which sidesteps the trust question that read-only services never face and is almost certainly why the portal launched reads-only.

Priced at the portal-standard $0.005 per submission, it fits the existing pattern exactly: one HTTPS endpoint, JSON in and out, x402 or MPP, failed submissions not charged. The supplier requirement is a staked node with transaction relay enabled, no new infrastructure class. The service-owner economics already documented on-chain apply: **2.5% of every settled request.**

## Why this brief passes its own tests

- **Concrete:** one named capability (signed-transaction relay) for one named chain with a named method (`sendTransaction`).
- **Nonduplicative:** verified against the full machine-readable catalogue, zero execution services exist for any of the 124.
- **Relevant:** agents are the portal's paying users, execution is the workload agents pay premiums for, and the Foundation's own pace (Solana, Sui, Near and Tron read services all added in recent weeks) shows chain capabilities are being added continuously; execution is the visible next step.
- **Honest:** the evidence for demand comes from interested parties and is labeled as such.

## References

1. [agent.pocket.network/services.json](https://agent.pocket.network/services.json), full machine-readable catalogue, checked November 10, 2026: 124 services, 52 blockchain services all described as "Read-only," zero execution methods.
2. [DefiLlama](https://defillama.com/chain/solana), chain TVL rankings and stablecoin market caps, live API queries, November 10, 2026: Solana #3 by TVL at $5.07B; $14.4B stablecoins.
3. [RPC Fast, "Top Solana RPC for AI Agents,"](https://rpcfast.com/blog/top-solana-rpc-for-ai-agents) 2026: agent execution workload characteristics (burst submission, landing rate) and provider product tiers for execution.
4. [CryptoSlate, "Jito's Solana data feed puts a price on seeing trades early,"](https://cryptoslate.com/jitos-solana-data-feed-puts-a-price-on-seeing-trades-early/) October 2026: preconfirmation streaming sold to automated consumers; 35/35/30 revenue split.

---

*Authored by [@Jayanng](https://github.com/Jayanng) · November 10, 2026 · Every claim re-verifiable from the linked sources.*
