---
layout: page
title: ChemLib
permalink: /chemlib/
nav_order: 4
---

# ChemLib - Compound Libraries

<div class="assay-grid">
  <div class="assay-card">
    <h2>Active Compound Library</h2>
    <p>Screened & validated active compounds for drug discovery.</p>
    <a href="/chemlib/active" class="btn">Browse →</a>
  </div>

  <div class="assay-card">
    <h2>Natural Product Library</h2>
    <p>Plant & microbial derived natural products.</p>
    <a href="/chemlib/natural" class="btn">Browse →</a>
  </div>

  <div class="assay-card">
    <h2>Novel Scaffold Library</h2>
    <p>Your in‑house novel scaffold compounds.</p>
    <a href="/chemlib/scaffold" class="btn">Browse →</a>
  </div>

  <div class="assay-card">
    <h2>Drug‑Like Library</h2>
    <p>High diversity drug‑like small molecules.</p>
    <a href="/chemlib/druglike" class="btn">Browse →</a>
  </div>
</div>

<style>
.assay-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin-top: 2rem;
}
.assay-card {
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  padding: 28px 24px;
  background: #fafbfc;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: 0.2s;
}
.assay-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}
.assay-card h2 {
  font-size: 19px;
  margin-bottom: 12px;
  color: #222;
}
.assay-card p {
  font-size: 15px;
  color: #555;
  line-height: 1.5;
  margin-bottom: 20px;
}
.assay-card .btn {
  color: #0066cc;
  font-weight: 500;
  text-decoration: none;
}
.assay-card .btn:hover {
  text-decoration: underline;
}
</style>