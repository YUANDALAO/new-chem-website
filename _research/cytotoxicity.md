---
layout: default
title: Research - Cytotoxicity & Viability Assays
permalink: /research/cell-assays/cytotoxicity/
---

<div class="container" style="padding: 2rem 0;">
  <!-- 移动端顶部间距适配（与父页面Cellular Assays保持样式统一） -->
  <style>
    @media (max-width: 768px) {
      .container {
        padding-top: 4rem !important; /* 与父页面一致的导航栏高度适配，确保移动端显示完整 */
      }

      /* 统一卡片样式，保持与父页面及其他子页面视觉一致性 */
      .research-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
      }

      .assay-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s;
        border-top: 3px solid #2980b9;
      }

      .assay-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(41, 128, 185, 0.15);
      }

      .specs-grid {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 1.5rem;
        margin: 2rem 0;
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 12px;
      }

      .spec-item {
        text-align: center;
        flex: 1;
        min-width: 150px;
      }

      .spec-number {
        font-size: 2.2em;
        font-weight: 800;
        color: #2980b9;
        display: block;
      }

      .spec-label {
        color: #666;
        font-size: 1em;
        margin-top: 0.5rem;
      }
    }

    /* 桌面端样式补充 */
    .research-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 2rem;
      margin-top: 2rem;
    }

    .assay-card {
      background: white;
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
      transition: all 0.3s;
      border-top: 3px solid #2980b9;
    }

    .assay-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 30px rgba(41, 128, 185, 0.15);
    }

    .section {
      margin: 4rem 0;
    }

    .section-title {
      font-size: 2em;
      font-weight: 700;
      color: #2c3e50;
      margin-bottom: 1.5rem;
      border-left: 5px solid #2980b9;
      padding-left: 1rem;
    }

    .specs-grid {
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin: 2rem 0;
      background: #f8f9fa;
      padding: 2rem;
      border-radius: 12px;
    }

    .spec-item {
      text-align: center;
      flex: 1;
      min-width: 150px;
    }

    .spec-number {
      font-size: 2.2em;
      font-weight: 800;
      color: #2980b9;
      display: block;
    }

    .spec-label {
      color: #666;
      font-size: 1em;
      margin-top: 0.5rem;
    }

    .validation-details {
      background: #f8f9fa;
      padding: 2rem;
      border-radius: 12px;
      margin: 2rem 0;
    }

    .back-link {
      display: inline-block;
      margin-top: 2rem;
      color: #2980b9;
      font-weight: 600;
      text-decoration: none;
      transition: color 0.3s;
    }

    .back-link:hover {
      color: #1a5a8c;
    }
  </style>

  <!-- 页面主标题与核心介绍 -->
  <h1>Cytotoxicity & Viability Assays</h1>
  <hr>
  <p style="font-size: 1.1em; line-height: 1.6;">
    Our cytotoxicity and viability assays provide quantitative evaluation of compound-induced cell damage and survival—critical for distinguishing therapeutic efficacy from toxicity in drug discovery. These assays are optimized for high reproducibility and throughput, supporting early-stage compound screening, lead optimization, and preclinical safety assessment for flavivirus inhibitors and other therapeutic candidates.
  </p>

  <!-- 核心检测方法板块（与父页面"Assay Types"逻辑呼应） -->
  <div class="section">
    <h2 class="section-title">Key Assay Technologies</h2>
    <div class="research-grid">
      <div class="assay-card">
        <h3>MTT & MTS Assays</h3>
        <p>Colorimetric detection of mitochondrial dehydrogenase activity to measure viable cell number. Optimized for 96/384-well formats with reduced background interference from small molecules.</p>
        <p style="margin-top: 1rem; color: #2980b9; font-weight: 500;">Readout: Absorbance (570 nm)</p>
      </div>

      <div class="assay-card">
        <h3>LDH Release Assay</h3>
        <p>Quantification of lactate dehydrogenase (LDH) leakage from damaged cells to assess membrane integrity. Validated for both adherent and suspension cell lines.</p>
        <p style="margin-top: 1rem; color: #2980b9; font-weight: 500;">Readout: Absorbance (490 nm)</p>
      </div>

      <div class="assay-card">
        <h3>Live/Dead Staining</h3>
        <p>Fluorescence-based dual staining (calcein-AM for live cells, ethidium homodimer for dead cells) for direct visualization and quantification of cell viability via high-content imaging.</p>
        <p style="margin-top: 1rem; color: #2980b9; font-weight: 500;">Readout: Fluorescence (Ex485/Em535, Ex528/Em617)</p>
      </div>

      <div class="assay-card">
        <h3>ATP Luminescence Assay</h3>
        <p>Ultra-sensitive detection of intracellular ATP (a marker of metabolically active cells) using luciferase-based luminescence. Ideal for low-cell-number samples and high-throughput screening.</p>
        <p style="margin-top: 1rem; color: #2980b9; font-weight: 500;">Readout: Luminescence (Relative Light Units)</p>
      </div>
    </div>
  </div>

  <!-- 技术参数板块 -->
  <div class="section">
    <h2 class="section-title">Assay Performance Specifications</h2>
    <div class="specs-grid">
      <div class="spec-item">
        <span class="spec-number">96/384</span>
        <span class="spec-label">Well Plate Formats</span>
      </div>
      <div class="spec-item">
        <span class="spec-number">24-72</span>
        <span class="spec-label">Incubation Hours</span>
      </div>
      <div class="spec-item">
        <span class="spec-number"><5%</span>
        <span class="spec-label">CV (Intra-Assay)</span>
      </div>
      <div class="spec-item">
        <span class="spec-number"><10%</span>
        <span class="spec-label">CV (Inter-Assay)</span>
      </div>
      <div class="spec-item">
        <span class="spec-number">100-10k</span>
        <span class="spec-label">Cells/Well (Optimal)</span>
      </div>
    </div>
  </div>

  <!-- 实验设计与验证板块 -->
  <div class="section">
    <h2 class="section-title">Assay Design & Validation</h2>
    <div class="validation-details">
      <ul style="line-height: 1.8; color: #555; padding-left: 1.5rem;">
        <li><strong>Dose-Response Profiling:</strong> Automated generation of IC50 values for compound cytotoxicity, with 8-10 concentration points per compound</li>
        <li><strong>Cell Line Specificity:</strong> Assays optimized for relevant cell models (e.g., Vero cells for flavivirus studies, HeLa/SH-SY5Y for human cell toxicity)</li>
        <li><strong>Positive Controls:</strong> Standardized controls (e.g., staurosporine, Triton X-100) to ensure assay robustness across batches</li>
        <li><strong>Media Interference Testing:</strong> Evaluation of compound solubility and media interaction to eliminate false-positive/negative results</li>
        <li><strong>Reproducibility Testing:</strong> Validation across multiple operators and equipment to meet GLP-compliant standards for preclinical studies</li>
      </ul>
    </div>
  </div>

  <!-- 研究应用板块 -->
  <div class="section">
    <h2 class="section-title">Research Applications</h2>
    <div class="research-grid">
      <div class="assay-card">
        <h3>Early-Stage Compound Screening</h3>
        <p>High-throughput assessment of cytotoxicity for large compound libraries to prioritize candidates with low toxicity profiles.</p>
      </div>
      <div class="assay-card">
        <h3>Therapeutic Index Calculation</h3>
        <p>Comparison of antiviral/therapeutic efficacy (EC50) vs. cytotoxicity (CC50) to determine therapeutic index (TI = CC50/EC50) for lead compounds.</p>
      </div>
      <div class="assay-card">
        <h3>Mechanism of Toxicity Studies</h3>
        <p>Combination with apoptosis/necrosis markers (e.g., caspase activation, reactive oxygen species) to distinguish cell death mechanisms induced by compounds.</p>
      </div>
      <div class="assay-card">
        <h3>In Vitro Safety Assessment</h3>
        <p>Evaluation of compound toxicity in primary human cells (e.g., hepatocytes, neurons) to predict in vivo safety profiles.</p>
      </div>
    </div>
  </div>

  <!-- 返回父页面链接 -->
  <a href="{{ '/research/cell-assays/' | relative_url }}" class="back-link">
    &larr; Back to Cellular Assays
  </a>
</div>