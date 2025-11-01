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
/* 假设导航栏类名为 .navbar，根据实际情况修改 */
.navbar {
  /* 固定导航栏时，需明确高度以便计算下方内容偏移 */
  height: 60px; /* 根据实际导航栏高度调整 */
  position: fixed; /* 或 sticky，取决于原导航栏实现 */
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000; /* 确保导航栏在最上层 */
}

/* 为内容容器添加顶部间距，避开导航栏 */
.container {
  /* 间距值 >= 导航栏高度，避免遮挡 */
  padding-top: 80px !important; /* 覆盖原有 2rem 并增加，根据导航栏高度调整 */
}

/* 移动端适配：针对小屏幕进一步调整 */
@media (max-width: 768px) {
  .navbar {
    height: 80px; /* 移动端导航栏可能更高（如换行），需调整 */
  }
  .container {
    padding-top: 100px !important; /* 适配移动端导航栏高度 */
  }
  .subsection-grid {
    /* 可选：减小移动端网格间距，避免内容过挤 */
    gap: 1rem;
    padding: 0 1rem; /* 增加左右内边距，避免内容贴边 */
  }
}
</style>
<div class="container" style="padding: 2rem 0;">
    <h1>AI-Powered Drug Discovery</h1>
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
        <h4>QSAR Predictive Modeling</h4>
        <p>Developing predictive models for Quantitative Structure-Activity Relationships.</p>
      </a>
      <a href="{{ '/research/ai/synthia/' | relative_url }}" class="subsection-card">
        <h4>AI for Synthetic Methodology</h4>
        <p>Developing AI models to optimize chemical synthesis routes and predict reaction outcomes.</p>
      </a>
      <a href="{{ '/research/ai/alphafold3/' | relative_url }}" class="subsection-card">
        <h4>AlphaFold3 Applications</h4>
        <p>Applying advanced protein structure prediction to identify novel drug targets.</p>
      </a>
      <a href="{{ '/research/ai/rfdiffusion/' | relative_url }}" class="subsection-card">
        <h4>RFdiffusion for Proteins</h4>
        <p>Designing novel protein binders and enzymes using generative diffusion models.</p>
      </a>
      <a href="{{ '/research/ai/aidd/' | relative_url }}" class="subsection-card">
        <h4>Structure-Based AIDD</h4>
        <p>Utilizing protein structures for AI-driven drug design, including docking and simulation.</p>
      </a>
      <a href="{{ '/research/ai/admet/' | relative_url }}" class="subsection-card">
        <h4>ADMET Prediction</h4>
        <p>Advanced models for predicting Absorption, Distribution, Metabolism, Excretion and Toxicity profiles.</p>
      </a>
      <a href="{{ '/research/ai/multiomics/' | relative_url }}" class="subsection-card">
        <h4>Multi-Omics Integration</h4>
        <p>Combining genomic, transcriptomic, and proteomic data to identify disease-specific drug targets.</p>
      </a>
      <a href="{{ '/research/ai/clinical-trial/' | relative_url }}" class="subsection-card">
        <h4>Clinical Trial Optimization</h4>
        <p>AI models to predict patient recruitment, trial outcomes, and adverse event likelihood.</p>
      </a>
      <a href="{{ '/research/ai/knowledge-graphs/' | relative_url }}" class="subsection-card">
        <h4>Biomedical Knowledge Graphs</h4>
        <p>Constructing semantic networks to uncover hidden relationships between drugs, targets and diseases.</p>
      </a>
      <a href="{{ '/research/ai/real-world-evidence/' | relative_url }}" class="subsection-card">
        <h4>Real-World Evidence Analysis</h4>
        <p>Leveraging AI to extract drug efficacy insights from heterogeneous real-world healthcare data.</p>
      </a>
    </div>
</div>