---
layout: default
title: Research - AI for Drug Discovery
---
<style>
  .subsection-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 1.5rem; }
  .subsection-card { border: 1px solid #e0e0e0; padding: 1.5rem; border-radius: 8px; text-decoration: none; color: inherit; display: block; transition: all 0.2s ease-in-out; }
  .subsection-card:hover { transform: translateY(-5px); box-shadow: 0 8px 12px rgba(0,0,0,0.1); border-color: #3498db; }
  .subsection-card h4 { margin-top: 0; color: #2c3e50; }
  .subsection-card p { font-size: 0.95em; line-height: 1.5; margin-bottom: 0; }
</style>
<div class="container" style="padding: 2rem 0;">
    <h1>AI for Drug Discovery</h1>
    <hr>
    <p style="font-size: 1.1em; line-height: 1.6;">
      We are pioneering the integration of artificial intelligence and machine learning with traditional medicinal chemistry. This interdisciplinary approach aims to accelerate the entire drug discovery pipeline. Explore our key research areas in AI below:
    </p>
    <div class="subsection-grid">
      <a href="{{ '/research/ai/gendd/' | relative_url }}" class="subsection-card">
        <h4>GenDD Platform</h4>
        <p>Our in-house platform for generative de novo molecular design and property prediction.</p>
      </a>
      <a href="{{ '/research/ai/qsar/' | relative_url }}" class="subsection-card">
        <h4>QSAR Modeling</h4>
        <p>Developing predictive models for Quantitative Structure-Activity Relationships.</p>
      </a>
      <a href="{{ '/research/ai/aidd/' | relative_url }}" class="subsection-card">
        <h4>Structure-Based AIDD</h4>
        <p>Utilizing protein structures for AI-driven drug design, including docking and simulation.</p>
      </a>
      <a href="{{ '/research/ai/alphafold3/' | relative_url }}" class="subsection-card">
        <h4>AlphaFold3 Applications</h4>
        <p>Applying advanced protein structure prediction to identify novel drug targets.</p>
      </a>
      <a href="{{ '/research/ai/rfdiffusion/' | relative_url }}" class="subsection-card">
        <h4>RFdiffusion for Proteins</h4>
        <p>Designing novel protein binders and enzymes using generative diffusion models.</p>
      </a>
    </div>
</div>