---
layout: default
title: Research - QSAR Modeling
permalink: /research/ai/qsar/
---
<!-- QSAR项目区块 -->

<style>
  /* 样式部分保持不变，因为它设计得很好 */
  .qsar-section { margin: 60px 0; padding: 50px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 16px; position: relative; overflow: hidden; }
  .qsar-section::before { content: '📈'; position: absolute; font-size: 15em; opacity: 0.05; right: -50px; top: -50px; transform: rotate(15deg); }
  .qsar-header { position: relative; z-index: 1; }
  .qsar-title { font-size: 2.8em; font-weight: 800; color: #1e3c72; margin-bottom: 10px; }
  .qsar-subtitle { font-size: 1.3em; color: #2a5298; font-weight: 600; margin-bottom: 25px; }
  .qsar-description { font-size: 1.1em; line-height: 1.8; color: #2c3e50; margin-bottom: 30px; position: relative; z-index: 1; }
  .qsar-features { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0; position: relative; z-index: 1; }
  .qsar-feature { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 3px 15px rgba(0,0,0,0.08); transition: all 0.3s; }
  .qsar-feature:hover { transform: translateY(-5px); box-shadow: 0 6px 25px rgba(30, 60, 114, 0.15); }
  .qsar-feature h4 { color: #1e3c72; font-size: 1.2em; margin-bottom: 10px; display: flex; align-items: center; gap: 10px; }
  .qsar-feature p { color: #555; line-height: 1.6; margin: 0; }
  .qsar-stats { display: flex; justify-content: space-around; margin: 40px 0; flex-wrap: wrap; position: relative; z-index: 1; }
  .qsar-stat { text-align: center; padding: 20px; }
  .qsar-stat-number { font-size: 2.5em; font-weight: 800; color: #1e3c72; display: block; }
  .qsar-stat-label { color: #555; font-size: 1em; margin-top: 5px; }
  .qsar-cta { text-align: center; margin-top: 40px; position: relative; z-index: 1; }
  .qsar-btn { display: inline-block; padding: 15px 40px; background: #1e3c72; color: white; text-decoration: none; border-radius: 30px; font-weight: 600; font-size: 1.1em; transition: all 0.3s; box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3); }
  .qsar-btn:hover { background: #2a5298; transform: translateY(-3px); box-shadow: 0 6px 25px rgba(30, 60, 114, 0.4); }
  @media (max-width: 768px) {
    .qsar-section { padding: 30px 20px; }
    .qsar-title { font-size: 2em; }
    .qsar-features { grid-template-columns: 1fr; }
  }
</style>

<div class="qsar-section">
  <div class="qsar-header">
    <h2 class="qsar-title">QSAR Modeling</h2>
    <p class="qsar-subtitle">Quantitative Structure-Activity Relationship</p>
  </div>

  <div class="qsar-description">
    <strong>QSAR modeling</strong> is a cornerstone of our computational chemistry efforts. We develop and validate robust predictive models that correlate the physicochemical properties of molecules with their biological activities. By leveraging machine learning algorithms—from classical methods like Random Forest to advanced Graph Neural Networks—we can accurately predict the potency, toxicity, and ADMET properties of novel compounds before they are ever synthesized.
  </div>

  <!-- 核心特性 -->
  <div class="qsar-features">
    <div class="qsar-feature">
      <h4>📊 Feature Engineering</h4>
      <p>Utilizing a wide range of molecular descriptors (1D to 3D) and fingerprints to capture the essence of molecular structure.</p>
    </div>

    <div class="qsar-feature">
      <h4>🤖 Advanced Algorithms</h4>
      <p>Applying state-of-the-art machine learning and deep learning models for superior predictive accuracy.</p>
    </div>

    <div class="qsar-feature">
      <h4>✅ Rigorous Validation</h4>
      <p>Employing cross-validation, external test sets, and Y-scrambling to ensure the reliability and robustness of our models.</p>
    </div>

    <div class="qsar-feature">
      <h4>🔍 Applicability Domain</h4>
      <p>Defining the chemical space where our models can make reliable predictions, ensuring scientific validity.</p>
    </div>
  </div>

  <!-- 统计数据 -->
  <div class="qsar-stats">
    <div class="qsar-stat">
      <span class="qsar-stat-number">200+</span>
      <span class="qsar-stat-label">Descriptors Used</span>
    </div>
    <div class="qsar-stat">
      <span class="qsar-stat-number">R² > 0.85</span>
      <span class="qsar-stat-label">Model Accuracy</span>
    </div>
    <div class="qsar-stat">
      <span class="qsar-stat-number">10k+</span>
      <span class="qsar-stat-label">Compounds Modeled</span>
    </div>
  </div>

  <!-- 应用领域 -->
  <div class="qsar-description" style="margin-top: 30px;">
    <strong>Primary Applications:</strong> Hit-to-lead optimization, virtual screening of large compound libraries, ADMET profiling, and guiding the design of analogs with improved activity and safety profiles.
  </div>

  <!-- CTA按钮 (返回AI主页) -->
  <div class="qsar-cta">
    <a href="{{ '/research/ai-driven-discovery/' | relative_url }}" class="qsar-btn">&larr; Back to AI for Drug Discovery</a>
  </div>
</div>