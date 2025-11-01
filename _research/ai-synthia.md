---
layout: default
title: Research - Synthia
permalink: /research/ai/synthia/
---

<style>
  /* Synthia专属样式 */
  .synthia-hero {
    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
    color: white;
    padding: 80px 20px;
    text-align: center;
    margin: -40px -40px 60px -40px;
    position: relative;
    overflow: hidden;
  }

  .synthia-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><path d="M10,50 Q50,10 90,50 T170,50" stroke="white" fill="none" stroke-width="1" opacity="0.1"/></svg>');
    animation: float 25s linear infinite;
  }

  @keyframes float {
    from { background-position: 0 0; }
    to { background-position: 100px 100px; }
  }

  .synthia-hero h1 {
    font-size: 3.5em;
    font-weight: 800;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;
  }

  .synthia-hero .tagline {
    font-size: 1.4em;
    opacity: 0.95;
    max-width: 700px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
  }

  .synthia-container {
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
    border-left: 5px solid #2980b9;
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
    border-top: 3px solid #2980b9;
  }

  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(41, 128, 185, 0.15);
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
    color: #2980b9;
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
    border-left: 4px solid #2980b9;
  }

  .step-number {
    font-size: 2em;
    font-weight: 800;
    color: #2980b9;
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

  .process-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 40px;
  }

  .process-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    text-align: center;
  }

  .process-card img {
    max-width: 100%;
    border-radius: 8px;
    margin-bottom: 15px;
  }

  .process-card h4 {
    color: #2c3e50;
    margin-bottom: 10px;
  }

  .cta-section {
    background: linear-gradient(135deg, #2980b9 0%, #3498db 100%);
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
    color: #2980b9;
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
    color: #2980b9;
  }

  @media (max-width: 768px) {
    .synthia-hero {
    /* 调整负边距，避免向上偏移过多 */
    margin: -20px -20px 40px -20px;
    /* 如果导航栏有固定高度（例如60px），添加对应补偿 */
    padding-top: 80px; /* 导航栏高度 + 额外间距 */
  }
    .synthia-hero h1 {
      font-size: 2.5em;
    }
    .features-grid, .process-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<!-- Hero区域 -->
<div class="synthia-hero">
  <h1>🧪 Synthia</h1>
  <p class="tagline">AI-Driven Synthetic Chemistry Platform<br>Revolutionizing Chemical Synthesis Design</p>
</div>

<div class="synthia-container">

  <!-- 项目概述 -->
  <div class="section">
    <h2 class="section-title">Project Overview</h2>
    <p style="font-size: 1.15em; line-height: 1.8; color: #555;">
      Synthia represents a breakthrough in synthetic chemistry, leveraging advanced artificial intelligence to transform the way chemical synthesis routes are designed and optimized. Our platform integrates large-scale knowledge distillation, rigorous predictive modeling, generative AI for de novo design, and robust interpretation frameworks to deliver actionable synthetic strategies for complex molecules.
    </p>
  </div>

  <!-- 统计数据 -->
  <div class="stats-bar">
    <div class="stat-item">
      <span class="stat-number">10K+</span>
      <span class="stat-label">Reactions Analyzed</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">92%</span>
      <span class="stat-label">Prediction Accuracy</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">500+</span>
      <span class="stat-label">Synthetic Routes Optimized</span>
    </div>
    <div class="stat-item">
      <span class="stat-number">80%</span>
      <span class="stat-label">Time Reduction in Route Design</span>
    </div>
  </div>

  <!-- 核心技术 -->
  <div class="section">
    <h2 class="section-title">Core Technologies</h2>
    <div class="features-grid">
      <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <h3>Large-Scale Knowledge Distillation</h3>
        <p>Curate and distill vast chemical reaction databases (Reaxys, USPTO, in-house data) into actionable synthetic knowledge.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h3>Rigorous Predictive Modeling</h3>
        <p>Develop machine learning models to predict reaction outcomes, yields, and selectivity with high precision.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>Generative AI for De Novo Design</h3>
        <p>Generate novel synthetic routes and retrosynthetic strategies using transformer-based generative architectures.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <h3>Interpretation & Validation</h3>
        <p>Explainable AI frameworks to validate predictions and derive chemical insights from model decisions.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">🔄</div>
        <h3>Retrosynthetic Planning</h3>
        <p>AI-driven backward synthesis planning to identify optimal starting materials and intermediate steps.</p>
      </div>

      <div class="feature-card">
        <div class="feature-icon">⚗️</div>
        <h3>Reaction Condition Optimization</h3>
        <p>Machine learning models to optimize solvents, catalysts, temperatures, and other reaction parameters.</p>
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
          <h4>Molecule Input</h4>
          <p>Upload target molecule structure or SMILES notation for synthesis route planning.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">02</div>
        <div class="step-content">
          <h4>Retrosynthetic Analysis</h4>
          <p>AI-powered backward decomposition to identify potential starting materials and intermediates.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">03</div>
        <div class="step-content">
          <h4>Route Evaluation</h4>
          <p>Multi-criteria scoring of candidate routes based on yield, cost, safety, and synthetic accessibility.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">04</div>
        <div class="step-content">
          <h4>Condition Optimization</h4>
          <p>Machine learning models suggest optimal reaction conditions for each step in the synthesis pathway.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">05</div>
        <div class="step-content">
          <h4>Experimental Validation</h4>
          <p>Execute lab-scale synthesis using AI-recommended protocols and feed results back to improve models.</p>
        </div>
      </div>

      <div class="workflow-step">
        <div class="step-number">06</div>
        <div class="step-content">
          <h4>Route Refinement</h4>
          <p>Incorporate experimental data to iteratively improve route recommendations and prediction accuracy.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- 应用领域 -->
  <div class="section">
    <h2 class="section-title">Application Areas</h2>
    <div class="features-grid">
      <div class="feature-card">
        <h3>💊 Pharmaceutical Synthesis</h3>
        <p>Optimized routes for active pharmaceutical ingredients (APIs) and drug intermediates.</p>
      </div>

      <div class="feature-card">
        <h3>🧪 Fine Chemicals</h3>
        <p>Efficient synthesis pathways for specialty chemicals, flavors, and fragrances.</p>
      </div>

      <div class="feature-card">
        <h3>🔬 Materials Science</h3>
        <p>Synthetic routes for advanced materials, polymers, and functional molecules.</p>
      </div>

      <div class="feature-card">
        <h3>🌱 Green Chemistry</h3>
        <p>Design of sustainable synthesis routes with reduced waste and environmental impact.</p>
      </div>
    </div>
  </div>

  <!-- 技术优势 -->
  <div class="section">
    <h2 class="section-title">Competitive Advantages</h2>
    <div style="background: #f8f9fa; padding: 40px; border-radius: 12px;">
      <ul style="font-size: 1.1em; line-height: 2; color: #555;">
        <li><strong>Speed:</strong> Reduce synthesis route development from months to days</li>
        <li><strong>Cost Efficiency:</strong> Identify cost-optimized pathways with lower reagent and energy requirements</li>
        <li><strong>Novelty:</strong> Discover non-obvious synthetic routes beyond human intuition</li>
        <li><strong>Scalability:</strong> Handle complex molecules with up to 50+ synthetic steps</li>
        <li><strong>Adaptability:</strong> Continuously learns from new reactions and experimental data</li>
        <li><strong>Accessibility:</strong> Makes advanced synthetic planning accessible to non-experts</li>
      </ul>
    </div>
  </div>

  <!-- 合作机会 -->
  <div class="cta-section">
    <h2>Transform Your Synthetic Workflow</h2>
    <p style="font-size: 1.2em; opacity: 0.95; max-width: 700px; margin: 0 auto;">
      Partner with us to integrate Synthia into your research pipeline. We offer customized solutions for pharmaceutical companies, chemical manufacturers, and academic laboratories.
    </p>
    <div class="cta-buttons">
      <a href="/contact/" class="cta-btn cta-btn-primary">Request Demo</a>
      <a href="/publications/" class="cta-btn cta-btn-secondary">View Case Studies</a>
    </div>
  </div>

</div>