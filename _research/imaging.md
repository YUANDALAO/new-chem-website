---
layout: default
title: Research - High-Content Imaging Assays
permalink: /research/cell-assays/imaging/
---

<div class="container" style="padding: 2rem 0; font-family: 'Segoe UI', Roboto, sans-serif;">
  <!-- 基础样式与移动端适配 -->
  <style>
    /* 移动端顶部间距适配（与父页面保持一致） */
    @media (max-width: 768px) {
      .container {
        padding-top: 4rem !important;
      }
      .imaging-grid {
        grid-template-columns: 1fr !important;
      }
      .workflow-step {
        flex-direction: column !important;
        text-align: center !important;
      }
      .step-number {
        margin-right: 0 !important;
        margin-bottom: 1rem !important;
      }
    }

    /* 全局动画定义 */
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes pulse {
      0%, 100% {
        box-shadow: 0 0 0 0 rgba(41, 128, 185, 0.4);
      }
      50% {
        box-shadow: 0 0 0 10px rgba(41, 128, 185, 0);
      }
    }

    @keyframes float {
      0%, 100% {
        transform: translateY(0);
      }
      50% {
        transform: translateY(-10px);
      }
    }

    /* 卡片基础样式 */
    .imaging-card {
      background: white;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      transition: all 0.3s ease;
      border-top: 3px solid #2980b9;
      opacity: 0;
      animation: fadeInUp 0.6s forwards;
    }

    .imaging-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 30px rgba(41, 128, 185, 0.15);
    }

    /* 网格布局 */
    .imaging-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 2rem;
      margin-top: 2rem;
    }

    /* 标题与文本样式 */
    .section-title {
      font-size: 2em;
      font-weight: 700;
      color: #2c3e50;
      margin-bottom: 1.5rem;
      border-left: 5px solid #2980b9;
      padding-left: 1rem;
      opacity: 0;
      animation: fadeInUp 0.4s forwards 0.2s;
    }

    .section-desc {
      font-size: 1.1em;
      line-height: 1.7;
      color: #555;
      margin-bottom: 2rem;
      opacity: 0;
      animation: fadeInUp 0.4s forwards 0.3s;
    }

    /* 技术参数样式 */
    .specs-card {
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      padding: 2rem;
      border-radius: 12px;
      margin: 2rem 0;
      opacity: 0;
      animation: fadeInUp 0.4s forwards 0.5s;
    }

    .specs-list {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      justify-content: space-between;
    }

    .spec-item {
      flex: 1;
      min-width: 200px;
      text-align: center;
    }

    .spec-value {
      font-size: 1.8em;
      font-weight: 800;
      color: #2980b9;
      margin-bottom: 0.5rem;
      animation: float 3s ease-in-out infinite;
    }

    .spec-label {
      color: #666;
      font-size: 1em;
    }

    /* 工作流程样式 */
    .workflow-container {
      margin: 3rem 0;
      opacity: 0;
      animation: fadeInUp 0.4s forwards 0.7s;
    }

    .workflow-step {
      display: flex;
      align-items: center;
      margin-bottom: 2rem;
      padding: 1.5rem;
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.05);
      transition: all 0.3s;
    }

    .workflow-step:hover {
      box-shadow: 0 4px 15px rgba(41, 128, 185, 0.1);
    }

    .step-number {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: #2980b9;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      margin-right: 1.5rem;
      animation: pulse 2s infinite;
    }

    .step-content h4 {
      color: #2c3e50;
      margin-bottom: 0.5rem;
    }

    .step-content p {
      color: #666;
      line-height: 1.6;
    }

    /* 应用场景样式 */
    .app-card {
      position: relative;
      overflow: hidden;
    }

    .app-card::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(180deg, rgba(41, 128, 185, 0) 0%, rgba(41, 128, 185, 0.05) 100%);
      z-index: 0;
      transition: all 0.5s;
    }

    .app-card:hover::after {
      background: linear-gradient(180deg, rgba(41, 128, 185, 0.1) 0%, rgba(41, 128, 185, 0.2) 100%);
    }

    .app-card h3, .app-card p {
      position: relative;
      z-index: 1;
    }

    /* 返回按钮样式 */
    .back-link {
      display: inline-block;
      margin-top: 3rem;
      padding: 0.8rem 2rem;
      background: #2980b9;
      color: white;
      border-radius: 30px;
      text-decoration: none;
      font-weight: 600;
      transition: all 0.3s;
      opacity: 0;
      animation: fadeInUp 0.4s forwards 0.9s;
    }

    .back-link:hover {
      background: #1a5a8c;
      transform: translateY(-3px);
      box-shadow: 0 4px 15px rgba(41, 128, 185, 0.3);
    }

    /* 图片容器样式（模拟成像数据展示） */
    .image-preview {
      margin: 2rem 0;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      opacity: 0;
      animation: fadeInUp 0.4s forwards 0.8s;
    }

    .image-placeholder {
      aspect-ratio: 1;
      border-radius: 8px;
      background: #f1f3f5;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
    }

    .image-placeholder img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s;
    }

    .image-placeholder:hover img {
      transform: scale(1.05);
    }

    .image-placeholder::before {
      content: 'Imaging Data';
      position: absolute;
      color: #666;
      font-size: 0.9em;
      z-index: 1;
      background: rgba(255,255,255,0.8);
      padding: 0.5rem 1rem;
      border-radius: 4px;
    }
  </style>

  <!-- 页面主标题与核心介绍 -->
  <h1>High-Content Imaging Assays</h1>
  <hr>
  <p class="section-desc">
    Our high-content imaging (HCI) assays combine automated fluorescence microscopy with advanced image analysis to capture multi-dimensional cellular phenotypes—enabling quantitative evaluation of compound effects on cell morphology, subcellular localization, and molecular expression. This technology is a cornerstone of our drug discovery pipeline, providing unparalleled insights into flavivirus infection mechanisms and therapeutic candidate efficacy.
  </p>

  <!-- 成像数据预览（带hover动画） -->
  <div class="image-preview">
    <div class="image-placeholder">
      <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 200 200'%3E%3Crect width='200' height='200' fill='%23e9ecef'/%3E%3Ccircle cx='100' cy='80' r='40' fill='%232980b9' opacity='0.6'/%3E%3Ccircle cx='70' cy='130' r='25' fill='%2327ae60' opacity='0.6'/%3E%3Ccircle cx='130' cy='140' r='30' fill='%23e74c3c' opacity='0.6'/%3E%3C/svg%3E" alt="Cellular imaging data">
    </div>
    <div class="image-placeholder">
      <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 200 200'%3E%3Crect width='200' height='200' fill='%23e9ecef'/%3E%3Cpath d='M50,100 Q100,50 150,100 Q100,150 50,100' fill='none' stroke='%232980b9' stroke-width='3' opacity='0.8'/%3E%3Cpath d='M60,110 Q100,70 140,110 Q100,150 60,110' fill='none' stroke='%2327ae60' stroke-width='2' opacity='0.7'/%3E%3Cpath d='M70,120 Q100,90 130,120 Q100,150 70,120' fill='none' stroke='%23e74c3c' stroke-width='1' opacity='0.6'/%3E%3C/svg%3E" alt="Subcellular localization">
    </div>
    <div class="image-placeholder">
      <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 200 200'%3E%3Crect width='200' height='200' fill='%23e9ecef'/%3E%3Crect x='40' y='40' width='40' height='40' rx='5' fill='%232980b9' opacity='0.6'/%3E%3Crect x='120' y='40' width='40' height='40' rx='5' fill='%232980b9' opacity='0.4'/%3E%3Crect x='40' y='120' width='40' height='40' rx='5' fill='%232980b9' opacity='0.5'/%3E%3Crect x='120' y='120' width='40' height='40' rx='5' fill='%232980b9' opacity='0.7'/%3E%3Ccircle cx='60' cy='60' r='8' fill='white'/%3E%3Ccircle cx='140' cy='60' r='8' fill='white'/%3E%3Ccircle cx='60' cy='140' r='8' fill='white'/%3E%3Ccircle cx='140' cy='140' r='8' fill='white'/%3E%3C/svg%3E" alt="Phenotypic screening">
    </div>
  </div>

  <!-- 核心技术能力（带渐入动画，卡片延迟错开） -->
  <div class="section">
    <h2 class="section-title">Core Imaging Capabilities</h2>
    <div class="imaging-grid">
      <div class="imaging-card" style="animation-delay: 0.2s;">
        <h3>Multi-Parameter Phenotyping</h3>
        <p>Simultaneous quantification of 10+ cellular features (e.g., cell area, nuclear shape, fluorescence intensity) to capture complex phenotypic changes induced by compounds or viral infection.</p>
      </div>
      <div class="imaging-card" style="animation-delay: 0.3s;">
        <h3>Subcellular Localization Tracking</h3>
        <p>High-resolution imaging of target proteins (e.g., viral antigens, signaling molecules) with subcellular precision, enabling analysis of translocation events and organelle-specific effects.</p>
      </div>
      <div class="imaging-card" style="animation-delay: 0.4s;">
        <h3>3D Cellular Imaging</h3>
        <p>Z-stack acquisition and 3D reconstruction to study cell behavior in 3D cultures (e.g., spheroids, organoids) — mimicking in vivo microenvironments for more physiologically relevant results.</p>
      </div>
      <div class="imaging-card" style="animation-delay: 0.5s;">
        <h3>Time-Lapse Imaging</h3>
        <p>Long-term live-cell imaging (up to 72 hours) to monitor dynamic cellular processes, including viral replication kinetics, cell migration, and compound-induced temporal responses.</p>
      </div>
    </div>
  </div>

  <!-- 技术参数（带悬浮动画） -->
  <div class="section">
    <h2 class="section-title">Imaging System Specifications</h2>
    <div class="specs-card">
      <div class="specs-list">
        <div class="spec-item">
          <div class="spec-value">4</div>
          <div class="spec-label">Fluorescence Channels</div>
        </div>
        <div class="spec-item">
          <div class="spec-value">0.5µm</div>
          <div class="spec-label">Spatial Resolution</div>
        </div>
        <div class="spec-item">
          <div class="spec-value">384-well</div>
          <div class="spec-label">Max Plate Format</div>
        </div>
        <div class="spec-item">
          <div class="spec-value">20min/plate</div>
          <div class="spec-label">Imaging Speed</div>
        </div>
        <div class="spec-item">
          <div class="spec-value">1000+</div>
          <div class="spec-label">Features/Cell</div>
        </div>
      </div>
    </div>
  </div>

  <!-- 工作流程（带步骤动画） -->
  <div class="section workflow-container">
    <h2 class="section-title">Assay Workflow</h2>
    <div class="workflow-step">
      <div class="step-number">1</div>
      <div class="step-content">
        <h4>Cell Preparation & Staining</h4>
        <p>Seeding of target cells (e.g., Vero, Huh7) in multi-well plates, followed by treatment with compounds/virus and staining with target-specific fluorophores (e.g., DAPI for nuclei, Alexa Fluor-conjugated antibodies for viral proteins).</p>
      </div>
    </div>
    <div class="workflow-step">
      <div class="step-number">2</div>
      <div class="step-content">
        <h4>Automated Imaging</h4>
        <p>High-throughput image acquisition using automated confocal or widefield microscopy, with adaptive focus and exposure control to ensure consistent image quality across plates.</p>
      </div>
    </div>
    <div class="workflow-step">
      <div class="step-number">3</div>
      <div class="step-content">
        <h4>Image Analysis</h4>
        <p>AI-powered image segmentation and feature extraction (using tools like CellProfiler, ImageJ) to quantify cellular and subcellular phenotypes, with custom algorithms for flavivirus-specific readouts.</p>
      </div>
    </div>
    <div class="workflow-step">
      <div class="step-number">4</div>
      <div class="step-content">
        <h4>Data Integration</h4>
        <p>Correlation of imaging data with other assay readouts (e.g., cytotoxicity, viral titer) to generate multi-dimensional datasets for compound prioritization and mechanism-of-action studies.</p>
      </div>
    </div>
  </div>

  <!-- 研究应用（带渐变背景动画） -->
  <div class="section">
    <h2 class="section-title">Key Research Applications</h2>
    <div class="imaging-grid">
      <div class="imaging-card app-card" style="animation-delay: 0.2s;">
        <h3>Flavivirus Infection Profiling</h3>
        <p>Quantification of viral replication (via NS3/NS5 protein expression), host cell morphology changes, and immune cell infiltration to evaluate antiviral compound efficacy.</p>
      </div>
      <div class="imaging-card app-card" style="animation-delay: 0.3s;">
        <h3>Phenotypic Screening</h3>
        <p>High-throughput screening of compound libraries to identify molecules that induce desired phenotypic changes (e.g., inhibition of viral assembly, restoration of normal cell morphology).</p>
      </div>
      <div class="imaging-card app-card" style="animation-delay: 0.4s;">
        <h3>Mechanism of Action Studies</h3>
        <p>Analysis of target protein localization (e.g., nuclear translocation of transcription factors) and organelle integrity (e.g., mitochondrial health) to elucidate how compounds exert their effects.</p>
      </div>
      <div class="imaging-card app-card" style="animation-delay: 0.5s;">
        <h3>Combination Therapy Testing</h3>
        <p>Evaluation of synergistic effects between multiple compounds using multi-parameter imaging, enabling optimization of combination treatment regimens.</p>
      </div>
    </div>
  </div>

  <!-- 返回父页面按钮（带hover动画） -->
  <a href="{{ '/research/cell-assays/' | relative_url }}" class="back-link">
    &larr; Back to Cellular Assays
  </a>
</div>