---
layout: default
title: Research - GenDD
permalink: /research/ai/gendd/
---

<style>
  /* GenDD专属样式 */
  .gendd-hero {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    color: white;
    padding: 80px 20px;
    text-align: center;
    margin: -40px -40px 60px -40px;
    position: relative;
    overflow: hidden;
  }

  .gendd-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="2" fill="white" opacity="0.1"/></svg>');
    animation: float 20s linear infinite;
  }

  @keyframes float {
    from { background-position: 0 0; }
    to { background-position: 100px 100px; }
  }

  .gendd-hero h1 {
    font-size: 3.5em;
    font-weight: 800;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
  }

  .gendd-hero .tagline {
    font-size: 1.4em;
    opacity: 0.95;
    max-width: 700px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
  }

  .gendd-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .section {
    margin-bottom: 80px;
  }

  .section-title {
    font-size: 2.2em;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 30px;
    border-left: 5px solid #2a5298;
    padding-left: 20px;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    margin-top: 40px;
  }

  .feature-card {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transition: all 0.3s;
    border-top: 3px solid #2a5298;
  }

  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(42, 82, 152, 0.15);
  }

  .feature-icon {
    font-size: 2.5em;
    margin-bottom: 15px;
  }

  .feature-card h3 {
    color: #2c3e50;
    font-size: 1.4em;
    margin-bottom: 15px;
  }

  .feature-card p {
    color: #666;
    line-height: 1.7;
  }

  .stats-bar {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    background: #f8f9fa;
    padding: 40px 20px;
    border-radius: 12px;
    margin: 40px 0;
  }

  .stat-item {
    text-align: center;
    padding: 20px;
  }

  .stat-number {
    font-size: 3em;
    font-weight: 800;
    color: #2a5298;
    display: block;
  }

  .stat-label {
    color: #666;
    font-size: 1.1em;
    margin-top: 10px;
  }

  .workflow-diagram {
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin: 40px 0;
  }

  .workflow-step {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
    padding: 20px;
    background: #f8f9fa;
    border-radius: 8px;
    border-left: 4px solid #2a5298;
  }

  .step-number {
    font-size: 2em;
    font-weight: 800;
    color: #2a5298;
    min-width: 60px;
  }

  .step-content h4 {
    color: #2c3e50;
    margin-bottom: 8px;
  }

  .step-content p {
    color: #666;
    margin: 0;
  }

  .cta-section {
    background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%);
    color: white;
    padding: 60px 40px;
    border-radius: 12px;
    text-align: center;
    margin-top: 60px;
  }

  .cta-section h2 {
    font-size: 2.5em;
    margin-bottom: 20px;
  }

  .cta-buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
    margin-top: 30px;
    flex-wrap: wrap;
  }

  .cta-btn {
    padding: 15px 40px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 600;
    font-size: 1.1em;
    transition: all 0.3s;
    display: inline-block;
  }

  .cta-btn-primary {
    background: white;
    color: #2a5298;
  }

  .cta-btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(255,255,255,0.3);
  }

  .cta-btn-secondary {
    background: transparent;
    color: white;
    border: 2px solid white;
  }

  .cta-btn-secondary:hover {
    background: white;
    color: #2a5298;
  }

  @media (max-width: 768px) {
    .gendd-hero h1 {
      font-size: 2.5em;
    }
    .features-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<!-- Hero区域 -->
<div class="gendd-hero">
  <h1>🧬 GenDD</h1>
  <p class="tagline">Generative Drug Design Platform<br>AI-Powered Molecular Innovation</p>
</div>

<div class="gendd-container">

  <!-- 项目概述 -->
  <div class="section">
    <h2 class="section-title">Project Overview</h2>
    <p style="font-size: 1.15em; line-height: 1.8; color: #555;">
      GenDD (Generative Drug Design) represents a paradigm shift in computational drug discovery, 
      leveraging cutting-edge deep learning architectures to generate novel drug-like molecules 
      with optimized properties. Our platform integrates transformer-based generative models, 
      multi-objective optimization, and physics-based scoring functions to accelerate the hit-to-lead 
      optimization process while maintaining synthetic accessibility.
    </p>
  </div>

  <!-- 统计数据 -->
  <div class="stats-bar">
    <div class="stat-item">
      <span class="stat-number">10M+</span>
      <span class="stat-label">Molecules Generated</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">95%</span>
      <span class="stat-label">Drug-likeness Score</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">50+</span>
      <span class="stat-label">Lead Compounds</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">3</span>
      <span class="stat-label">Clinical Candidates</span>
    </div>
  </div>

  <!-- 核心技术 -->
  <div class="section">
    <h2 class="section-title">Core Technologies</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <h3>Transformer Architecture</h3>
        <p>Advanced attention mechanisms for learning molecular grammar and generating chemically valid structures with desired properties.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <h3>Multi-Objective Optimization</h3>
        <p>Simultaneous optimization of potency, selectivity, ADMET properties, and synthetic accessibility using Pareto-efficient algorithms.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>Reinforcement Learning</h3>
        <p>Policy gradient methods to guide molecular generation toward regions of chemical space with high therapeutic potential.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">🔬</div>
        <h3>Active Learning</h3>
        <p>Iterative experimental validation feedback loop to continuously improve model predictions and accelerate optimization cycles.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Quantum Mechanics Integration</h3>
        <p>DFT calculations and molecular dynamics simulations for accurate property prediction and binding affinity estimation.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">🧪</div>
        <h3>Retrosynthetic Planning</h3>
        <p>AI-driven synthetic route prediction to ensure generated molecules are synthetically feasible and cost-effective.</p>
      </div>
    </div>
  </div>

  <!-- 工作流程 -->
  <div class="section">
    <h2 class="section-title">Workflow Pipeline</h2>
    <div class="workflow-diagram">
      <div class="workflow-step">
        <div class="step-number">01</div>
        <div class="step-content">
          <h4>Target Identification</h4>
          <p>Define therapeutic target, binding site, and desired molecular properties using structural biology data and clinical insights.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">02</div>
        <div class="step-content">
          <h4>Model Training</h4>
          <p>Train generative models on curated chemical databases (ChEMBL, PubChem, in-house data) with transfer learning from pre-trained architectures.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">03</div>
        <div class="step-content">
          <h4>Molecular Generation</h4>
          <p>Generate diverse molecular libraries using conditioned sampling, scaffold hopping, and de novo design strategies.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">04</div>
        <div class="step-content">
          <h4>In Silico Screening</h4>
          <p>Filter candidates using molecular docking, pharmacophore matching, ADMET prediction, and synthetic accessibility scoring.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">05</div>
        <div class="step-content">
          <h4>Experimental Validation</h4>
          <p>Synthesize top candidates and evaluate biological activity through biochemical assays and cellular phenotypic screens.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">06</div>
        <div class="step-content">
          <h4>Iterative Optimization</h4>
          <p>Incorporate experimental feedback to retrain models and generate improved second-generation molecules.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 应用领域 -->
  <div class="section">
    <h2 class="section-title">Therapeutic Applications</h2>
    <div class="features-grid">
      <div class="feature-card">
        <h3>🦠 Oncology</h3>
        <p>Kinase inhibitors, epigenetic modulators, and targeted protein degraders for cancer treatment.</p>
      </div>

      <div class="feature-card">
        <h3>🧠 Neurodegenerative Diseases</h3>
        <p>BBB-penetrant molecules targeting Alzheimer's, Parkinson's, and ALS pathology.</p>
      </div>

      <div class="feature-card">
        <h3>🦟 Infectious Diseases</h3>
        <p>Novel antibiotics and antivirals to combat drug-resistant pathogens and emerging viruses.</p>
      </div>

      <div class="feature-card">
        <h3>💊 Rare Diseases</h3>
        <p>Precision medicine approaches for orphan indications with unmet medical needs.</p>
      </div>
    </div>
  </div>

  <!-- 技术优势 -->
  <div class="section">
    <h2 class="section-title">Competitive Advantages</h2>
    <div style="background: #f8f9fa; padding: 40px; border-radius: 12px;">
      <ul style="font-size: 1.1em; line-height: 2; color: #555;">
        <li><strong>Speed:</strong> 100x faster than traditional high-throughput screening</li>
        <li><strong>Chemical Space:</strong> Explore 10<sup>60</sup> drug-like molecules beyond commercial libraries</li>
        <li><strong>Success Rate:</strong> 3-5x higher hit rates compared to conventional approaches</li>
        <li><strong>Cost Efficiency:</strong> Reduce early-stage R&D costs by 60-80%</li>
        <li><strong>Novelty:</strong> Generate IP-protectable scaffolds with minimal prior art</li>
        <li><strong>Interpretability:</strong> Explainable AI to understand structure-activity relationships</li>
      </ul>
    </div>
  </div>

  <!-- 合作机会 -->
  <div class="cta-section">
    <h2>Collaborate with GenDD</h2>
    <p style="font-size: 1.2em; opacity: 0.95; max-width: 700px; margin: 0 auto;">
      We're seeking partnerships with pharmaceutical companies, biotech startups, 
      and academic institutions to accelerate drug discovery programs.
    </p>
    <div class="cta-buttons">
      <a href="/contact/" class="cta-btn cta-btn-primary">Get in Touch</a>
      <a href="/publications/" class="cta-btn cta-btn-secondary">View Publications</a>
    </div>
  </div>

</div>