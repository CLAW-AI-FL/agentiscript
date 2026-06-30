#!/usr/bin/env python3
"""Generate new AgentiScript icons for agentic ops + payments expansion."""

import json
from pathlib import Path

ICONS_DIR = Path("/Users/colin/seo/agentiscript/icons")
BASE_DIR = Path("/Users/colin/seo/agentiscript")
COLOR = "#9F792C"

# Check existing
existing = {f.stem for f in ICONS_DIR.glob("*.json")}

icons = [
    # ─── COMPUTING ───────────────────────────────────────────────────────────
    {
        "slug": "zero-knowledge-ml",
        "concept": "Zero-Knowledge ML",
        "label": "Zero-Knowledge ML",
        "definition": "Machine learning inference or training performed within zero-knowledge proof systems, enabling model outputs to be verified without exposing weights or private inputs",
        "aliases": ["zkML", "zk machine learning", "private inference", "verifiable ML"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["zero knowledge", "machine learning", "privacy", "verification", "zkML"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M12 3 L21 7.5 L21 16.5 L12 21 L3 16.5 L3 7.5 Z"/>'
            f'<circle cx="12" cy="12" r="3"/>'
            f'<path d="M12 9 L8 6.5 M12 15 L16 17.5"/>'
            f'<path d="M9 12 L5 12 M15 12 L19 12"/>'
            f'<text x="12" y="13" text-anchor="middle" font-size="3.5" font-family="monospace" fill="{COLOR}" stroke="none">ZK</text>'
            f'</svg>'
        ),
    },
    {
        "slug": "verifiable-inference",
        "concept": "Verifiable Inference",
        "label": "Verifiable Inference",
        "definition": "AI inference where the computation is accompanied by a cryptographic proof that allows anyone to verify the output was produced correctly by a specific model",
        "aliases": ["proven inference", "auditable AI", "trustless AI inference", "proof of computation"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["verifiable", "inference", "cryptographic proof", "trustless", "AI"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="3" y="4" width="13" height="16" rx="2"/>'
            f'<path d="M7 8h5 M7 11h4 M7 14h6"/>'
            f'<circle cx="18" cy="16" r="3.5"/>'
            f'<path d="M16.5 16 l1 1.2 l2-2.2" stroke-width="1.2"/>'
            f'<path d="M14 5 l2 0" stroke-dasharray="1 1"/>'
            f'</svg>'
        ),
    },
    # ─── PAYMENTS / ECONOMY ──────────────────────────────────────────────────
    {
        "slug": "attention-economy",
        "concept": "Attention Economy",
        "label": "Attention Economy",
        "definition": "An economic model treating human or AI attention as a scarce resource, where platforms and agents compete to capture, direct, and monetize attention flows",
        "aliases": ["attention markets", "engagement economy", "attention as currency", "eyeball economy"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "tags": ["attention", "economy", "engagement", "monetization", "media"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<ellipse cx="12" cy="12" rx="9" ry="5"/>'
            f'<circle cx="12" cy="12" r="2.5"/>'
            f'<circle cx="12" cy="12" r="1" stroke-width="1"/>'
            f'<path d="M12 4 v-2 M12 22 v-2 M3 12 h-1 M22 12 h-1"/>'
            f'<path d="M5 19 l3-3 M19 5 l-3 3 M5 5 l3 3 M19 19 l-3-3" stroke-width="1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "creator-economy",
        "concept": "Creator Economy",
        "label": "Creator Economy",
        "definition": "An economic ecosystem where individual creators—including AI agents—generate, distribute, and monetize content or services directly, often through platform-independent channels",
        "aliases": ["content creator economy", "independent creator", "creator monetization", "creator platforms"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "tags": ["creator", "economy", "content", "monetization", "platform"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M12 3 l1.5 4.5 h4.5 l-3.5 2.5 1.5 4.5 L12 12 l-4 2.5 1.5-4.5 L6 7.5 h4.5 Z"/>'
            f'<circle cx="12" cy="12" r="0.5" stroke-width="1"/>'
            f'<path d="M12 15 v3 M9 19 q3-1 6 0" stroke-linecap="round"/>'
            f'<path d="M7 15 l-2 2 M17 15 l2 2"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "gig-economy",
        "concept": "Gig Economy",
        "label": "Gig Economy",
        "definition": "A labor market characterized by short-term, on-demand task contracts rather than permanent employment, extended to AI agents performing discrete tasks for hire",
        "aliases": ["freelance economy", "on-demand economy", "task economy", "agent gig market"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "tags": ["gig", "economy", "freelance", "on-demand", "tasks"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="3" y="7" width="18" height="12" rx="2"/>'
            f'<path d="M8 7 V5 a4 4 0 0 1 8 0 v2"/>'
            f'<path d="M8 13 h8 M12 11 v4"/>'
            f'<circle cx="6" cy="13" r="1.5"/>'
            f'<circle cx="18" cy="13" r="1.5"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "platform-economy",
        "concept": "Platform Economy",
        "label": "Platform Economy",
        "definition": "An economic model built on multi-sided platforms that facilitate interactions between producers and consumers—including AI agents—capturing value through network effects and transaction mediation",
        "aliases": ["platform business", "two-sided market", "marketplace economy", "network platform"],
        "category": "economics-finance",
        "category_name": "Economics & Finance",
        "tags": ["platform", "economy", "marketplace", "network effects", "two-sided market"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="3" y="14" width="5" height="6" rx="1"/>'
            f'<rect x="9.5" y="4" width="5" height="16" rx="1"/>'
            f'<rect x="16" y="10" width="5" height="10" rx="1"/>'
            f'<path d="M5.5 14 L12 4 L18.5 10" stroke-dasharray="2 1"/>'
            f'</svg>'
        ),
    },
    # ─── INFRASTRUCTURE ──────────────────────────────────────────────────────
    {
        "slug": "service-mesh",
        "concept": "Service Mesh",
        "label": "Service Mesh",
        "definition": "A dedicated infrastructure layer that handles service-to-service communication in microservices architectures, providing observability, security, and traffic management",
        "aliases": ["sidecar proxy", "Istio", "Linkerd", "service-to-service networking"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["service mesh", "microservices", "networking", "infrastructure", "proxy"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="12" cy="12" r="2"/>'
            f'<circle cx="4" cy="5" r="1.5"/>'
            f'<circle cx="20" cy="5" r="1.5"/>'
            f'<circle cx="4" cy="19" r="1.5"/>'
            f'<circle cx="20" cy="19" r="1.5"/>'
            f'<circle cx="12" cy="2.5" r="1.5"/>'
            f'<circle cx="12" cy="21.5" r="1.5"/>'
            f'<path d="M12 10 L5.2 6.1 M12 10 L18.8 6.1 M12 14 L5.2 17.9 M12 14 L18.8 17.9 M12 10 L12 4 M12 14 L12 20" stroke-width="1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "api-gateway",
        "concept": "API Gateway",
        "label": "API Gateway",
        "definition": "A server that acts as the single entry point for all client requests, routing them to appropriate microservices while handling authentication, rate limiting, and protocol translation",
        "aliases": ["API proxy", "gateway service", "API management", "reverse proxy gateway"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["API gateway", "routing", "microservices", "authentication", "infrastructure"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="9" y="9" width="6" height="6" rx="1"/>'
            f'<path d="M3 6 h3 M3 12 h3 M3 18 h3"/>'
            f'<path d="M18 6 h3 M18 12 h3 M18 18 h3"/>'
            f'<path d="M6 6 L9 10 M6 12 L9 12 M6 18 L9 14"/>'
            f'<path d="M15 10 L18 6 M15 12 L18 12 M15 14 L18 18"/>'
            f'<circle cx="4.5" cy="6" r="1.5" stroke-width="1"/>'
            f'<circle cx="4.5" cy="12" r="1.5" stroke-width="1"/>'
            f'<circle cx="4.5" cy="18" r="1.5" stroke-width="1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "circuit-breaker",
        "concept": "Circuit Breaker",
        "label": "Circuit Breaker",
        "definition": "A resilience design pattern that detects failures in downstream services and short-circuits requests to prevent cascade failures, allowing the system to recover gracefully",
        "aliases": ["fault tolerance", "fallback pattern", "resilience pattern", "trip breaker"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["circuit breaker", "resilience", "fault tolerance", "microservices", "pattern"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M3 12 h4"/>'
            f'<path d="M7 12 L10 7"/>'
            f'<circle cx="10" cy="12" r="0.5"/>'
            f'<path d="M14 12 h7"/>'
            f'<circle cx="14" cy="12" r="1.5"/>'
            f'<path d="M12 6 l1.5 3 -3 3 1.5 3 -1.5 3" stroke-width="1.2"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "bulkhead-pattern",
        "concept": "Bulkhead Pattern",
        "label": "Bulkhead Pattern",
        "definition": "A resilience design pattern that isolates elements of an application into pools so that if one fails, others continue to function—inspired by ship bulkheads that prevent flooding",
        "aliases": ["bulkhead isolation", "resource isolation", "thread pool isolation", "fault isolation"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["bulkhead", "resilience", "isolation", "pattern", "microservices"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="2" y="4" width="20" height="16" rx="2"/>'
            f'<line x1="9" y1="4" x2="9" y2="20" stroke-width="2"/>'
            f'<line x1="15" y1="4" x2="15" y2="20" stroke-width="2"/>'
            f'<circle cx="5.5" cy="12" r="2"/>'
            f'<circle cx="12" cy="12" r="2"/>'
            f'<circle cx="18.5" cy="12" r="2"/>'
            f'<path d="M5.5 12 v-2 M12 12 v-2" stroke-width="1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "saga-pattern",
        "concept": "Saga Pattern",
        "label": "Saga Pattern",
        "definition": "A distributed transaction management pattern where a sequence of local transactions is coordinated via events or commands, with compensating transactions to handle failures",
        "aliases": ["saga orchestration", "choreography saga", "distributed saga", "compensating transaction"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["saga", "distributed transactions", "microservices", "pattern", "orchestration"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="2" y="5" width="4" height="4" rx="1"/>'
            f'<rect x="10" y="5" width="4" height="4" rx="1"/>'
            f'<rect x="18" y="5" width="4" height="4" rx="1"/>'
            f'<rect x="6" y="15" width="4" height="4" rx="1"/>'
            f'<rect x="14" y="15" width="4" height="4" rx="1"/>'
            f'<path d="M6 7 h4 M14 7 h4"/>'
            f'<path d="M4 9 L8 15 M12 9 L10 15 M12 9 L16 15 M20 9 L18 15"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "event-sourcing",
        "concept": "Event Sourcing",
        "label": "Event Sourcing",
        "definition": "An architectural pattern where application state is derived by replaying an immutable log of domain events rather than storing current state directly, enabling auditability and time-travel queries",
        "aliases": ["event log", "event store", "append-only log", "event replay"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["event sourcing", "events", "immutable log", "architecture", "CQRS"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="2" y="3" width="20" height="4" rx="1"/>'
            f'<rect x="2" y="9" width="20" height="4" rx="1"/>'
            f'<rect x="2" y="15" width="20" height="4" rx="1"/>'
            f'<circle cx="5" cy="5" r="0.8" stroke-width="1"/>'
            f'<circle cx="5" cy="11" r="0.8" stroke-width="1"/>'
            f'<circle cx="5" cy="17" r="0.8" stroke-width="1"/>'
            f'<path d="M8 5 h10 M8 11 h8 M8 17 h12" stroke-width="1"/>'
            f'<path d="M19 20 v3 M17 22 l2-2 2 2" stroke-width="1.2"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "cqrs",
        "concept": "CQRS",
        "label": "CQRS",
        "definition": "Command Query Responsibility Segregation: an architectural pattern that separates read (query) and write (command) operations into distinct models, enabling independent scaling and optimization",
        "aliases": ["command query responsibility segregation", "read write separation", "command model", "query model"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["CQRS", "command", "query", "architecture", "pattern"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="2" y="4" width="8" height="6" rx="1.5"/>'
            f'<rect x="14" y="4" width="8" height="6" rx="1.5"/>'
            f'<rect x="8" y="14" width="8" height="6" rx="1.5"/>'
            f'<path d="M6 10 L12 14 M18 10 L12 14"/>'
            f'<text x="6" y="8.5" text-anchor="middle" font-size="4" font-family="monospace" fill="{COLOR}" stroke="none">CMD</text>'
            f'<text x="18" y="8.5" text-anchor="middle" font-size="4" font-family="monospace" fill="{COLOR}" stroke="none">QRY</text>'
            f'</svg>'
        ),
    },
    {
        "slug": "distributed-tracing",
        "concept": "Distributed Tracing",
        "label": "Distributed Tracing",
        "definition": "A monitoring technique that tracks requests across multiple microservices or agents, recording timing and causality to diagnose latency, failures, and performance bottlenecks",
        "aliases": ["request tracing", "span tracing", "OpenTelemetry tracing", "Jaeger tracing"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["distributed tracing", "observability", "spans", "microservices", "monitoring"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<line x1="3" y1="6" x2="21" y2="6"/>'
            f'<line x1="5" y1="10" x2="18" y2="10"/>'
            f'<line x1="7" y1="14" x2="15" y2="14"/>'
            f'<line x1="9" y1="18" x2="17" y2="18"/>'
            f'<circle cx="3" cy="6" r="1.2" stroke-width="1"/>'
            f'<circle cx="21" cy="6" r="1.2" stroke-width="1"/>'
            f'<circle cx="5" cy="10" r="1.2" stroke-width="1"/>'
            f'<circle cx="18" cy="10" r="1.2" stroke-width="1"/>'
            f'<path d="M3 6 L5 10 M21 6 L18 10" stroke-width="1" stroke-dasharray="2 1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "observability-platform",
        "concept": "Observability Platform",
        "label": "Observability Platform",
        "definition": "An integrated system for collecting, storing, and analyzing metrics, logs, and traces from distributed systems, providing deep insight into system behavior and performance",
        "aliases": ["monitoring platform", "telemetry platform", "SRE platform", "OpenTelemetry"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["observability", "monitoring", "metrics", "logs", "traces"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="2" y="2" width="20" height="20" rx="2"/>'
            f'<path d="M6 16 L9 10 L12 13 L15 7 L18 11" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<line x1="2" y1="19" x2="22" y2="19" stroke-width="1"/>'
            f'<circle cx="15" cy="7" r="1.2" stroke-width="1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "chaos-engineering",
        "concept": "Chaos Engineering",
        "label": "Chaos Engineering",
        "definition": "The practice of deliberately injecting failures and perturbations into a system to discover weaknesses before they cause outages, pioneered by Netflix's Chaos Monkey",
        "aliases": ["chaos monkey", "fault injection", "resilience testing", "game days"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["chaos engineering", "fault injection", "resilience", "testing", "SRE"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M12 3 L4 7 L4 17 L12 21 L20 17 L20 7 Z"/>'
            f'<path d="M9 9 l6 6 M15 9 l-6 6" stroke-width="2"/>'
            f'<path d="M12 3 v3 M12 18 v3 M4 7 l-2-1 M20 7 l2-1" stroke-width="1" stroke-dasharray="2 1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "blue-green-deployment",
        "concept": "Blue-Green Deployment",
        "label": "Blue-Green Deployment",
        "definition": "A deployment strategy that maintains two identical production environments (blue and green), switching traffic between them to achieve zero-downtime releases and instant rollback capability",
        "aliases": ["blue green deploy", "zero-downtime deployment", "environment switching", "traffic switchover"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["blue-green", "deployment", "zero-downtime", "DevOps", "rollback"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="2" y="14" width="8" height="6" rx="1.5"/>'
            f'<rect x="14" y="14" width="8" height="6" rx="1.5"/>'
            f'<rect x="8" y="4" width="8" height="5" rx="1.5"/>'
            f'<path d="M12 9 v5"/>'
            f'<path d="M12 14 L6 14 M12 14 L18 14"/>'
            f'<path d="M6 14 v0"/>'
            f'<circle cx="6" cy="10" r="0.5" stroke-width="1"/>'
            f'<circle cx="18" cy="10" r="0.5" stroke-width="1"/>'
            f'<path d="M9 6.5 h6 M9 7.5 h5" stroke-width="1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "canary-deployment",
        "concept": "Canary Deployment",
        "label": "Canary Deployment",
        "definition": "A deployment technique that gradually rolls out changes to a small subset of users before full release, monitoring for errors and allowing quick rollback if issues are detected",
        "aliases": ["canary release", "gradual rollout", "progressive delivery", "canary testing"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["canary", "deployment", "gradual rollout", "progressive delivery", "DevOps"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<circle cx="12" cy="8" r="3"/>'
            f'<path d="M12 5 L12 3"/>'
            f'<path d="M9.5 6.5 L8 5 M14.5 6.5 L16 5"/>'
            f'<path d="M9 11 L5 19 h14 L15 11"/>'
            f'<path d="M8 19 h2 M11 15 h3 M14 19 h2" stroke-width="1"/>'
            f'<path d="M5 16 q3.5 -2 7 0 q3.5 2 7 0" stroke-width="1" stroke-dasharray="2 1"/>'
            f'</svg>'
        ),
    },
    {
        "slug": "feature-flag",
        "concept": "Feature Flag",
        "label": "Feature Flag",
        "definition": "A software development technique enabling features to be toggled on or off at runtime without code deployment, facilitating A/B testing, gradual rollouts, and kill switches",
        "aliases": ["feature toggle", "feature switch", "LaunchDarkly", "runtime toggle"],
        "category": "science-tech",
        "category_name": "Science & Tech",
        "tags": ["feature flag", "feature toggle", "A/B testing", "DevOps", "deployment"],
        "svg": (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{COLOR}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<line x1="5" y1="3" x2="5" y2="21"/>'
            f'<path d="M5 4 L19 4 L15 9 L19 14 L5 14" stroke-linejoin="round"/>'
            f'<rect x="8" y="17" width="8" height="3.5" rx="1.75"/>'
            f'<circle cx="14" cy="18.75" r="1.2" stroke-width="1"/>'
            f'</svg>'
        ),
    },
]

# Filter out already existing
new_icons = [ic for ic in icons if ic["slug"] not in existing]
print(f"Total to generate: {len(new_icons)}")
print(f"Already existing (skipped): {len(icons) - len(new_icons)}")

generated = []
for ic in new_icons:
    slug = ic["slug"]
    
    # Write JSON
    json_data = {
        "name": slug,
        "label": ic["label"],
        "concept": ic["concept"],
        "definition": ic["definition"],
        "aliases": ic.get("aliases", []),
        "category": ic["category"],
        "category_name": ic["category_name"],
        "tags": ic["tags"],
        "version": "1.5",
    }
    json_path = ICONS_DIR / f"{slug}.json"
    json_path.write_text(json.dumps(json_data, indent=2))
    
    # Write SVG
    svg_path = ICONS_DIR / f"{slug}.svg"
    svg_path.write_text(ic["svg"])
    
    generated.append(slug)
    print(f"  ✓ {slug}")

print(f"\nGenerated {len(generated)} new icons")

# ── Rebuild agentiscript.json ────────────────────────────────────────────────
print("\nRebuilding agentiscript.json...")
icons_dir = ICONS_DIR
all_json = sorted(icons_dir.glob("*.json"))
icon_entries = []
for jf in all_json:
    try:
        data = json.loads(jf.read_text())
        # Ensure svg field
        data["svg"] = f"/icons/{jf.stem}.svg"
        icon_entries.append(data)
    except Exception as e:
        print(f"  Warning: {jf.name}: {e}")

import datetime
output = {
    "version": "1.5",
    "total": len(icon_entries),
    "generated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "icons": icon_entries,
}
out_path = BASE_DIR / "agentiscript.json"
out_path.write_text(json.dumps(output, indent=2))
print(f"Rebuilt agentiscript.json with {len(icon_entries)} icons")
