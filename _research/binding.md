---
layout: default
title: Molecular Binding Assays
permalink: /research/chemical-assays/binding/
---

<style>
  /* 保持与主化学检测页面样式统一 */
  .binding-hero {
    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
    color: white;
    padding: 60px 20px;
    text-align: center;
    margin: -20px -20px 40px -20px;
    border-radius: 8px;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .section {
    margin-bottom: 60px;
    padding: 20px;
  }

  .section-title {
    font-size: 1.8em;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 25px;
    border-left: 4px solid #2980b9;
    padding-left: 15px;
  }

  .assay-types {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
    margin: 30px 0;
  }

  .assay-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.07);
    padding: 25px;
    transition: transform 0.3s ease;
  }

  .assay-card:hover {
    transform: translateY(-5px);
  }

  .assay-card h3 {
    color: #2980b9;
    margin-top: 0;
  }

  .tech-details {
    background: #f8f9fa;
    padding: 25px;
    border-radius: 8px;
    margin: 20px 0;
  }

  .application-list {
    list-style-type: none;
    padding: 0;
  }

  .application-list li {
    padding: 10px 0;
    border-bottom: 1px solid #eee;
    display: flex;
    align-items: flex-start;
  }

  .application-list li:before {
    content: "•";
    color: #2980b9;
    font-weight: bold;
    font-size: 1.5em;
    margin-right: 10px;
    line-height: 0.8;
  }

  .cta-section {
    background: #f8f9fa;
    padding: 40px;
    border-radius: 8px;
    text-align: center;
  }

  .cta-btn {
    display: inline-block;
    background: #2980b9;
    color: white;
    padding: 12px 30px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: 600;
    margin-top: 15px;
    transition: background 0.3s;
  }

  .cta-btn:hover {
    background: #1f6dad;
  }

  @media (max-width: 768px) {
    .container {
      padding-top: 4rem !important;
    }
    
    .binding-hero {
      margin: 0 -20px 30px -20px;
      padding: 40px 20px;
    }
  }
</style>

<div class="container" style="padding: 2rem 0;">
  <!-- 移动端适配 -->
  <style>
    @media (max-width: 768px) {
      .container {
        padding-top: 4rem !important;
      }
    }
  </style>

  <!-- 页面头部 -->
  <div class="binding-hero">
    <h1>Molecular Binding Assays</h1>
    <p style="font-size: 1.2em; max-width: 800px; margin: 0 auto;">Quantifying biomolecular interactions with high precision for drug discovery and target validation</p>
  </div>

  <!-- 概述部分 -->
  <div class="section">
    <p style="font-size: 1.1em; line-height: 1.7; color: #555;">
      Our molecular binding assays provide quantitative measurements of interactions between small molecules, peptides, and proteins—critical for identifying promising drug candidates and understanding their mechanism of action. These assays enable precise determination of binding affinity (Kd), specificity, and kinetic parameters (kon/koff) to support rational drug design and target validation.
    </p>
  </div>

  <!-- 检测方法类型 -->
  <div class="section">
    <h2 class="section-title">Assay Technologies</h2>
    <div class="assay-types">
      <div class="assay-card">
        <h3>Fluorescence-Based Assays</h3>
        <p>Homogeneous and heterogeneous fluorescence assays including FRET, TR-FRET, and fluorescence polarization techniques for rapid screening of compound libraries.</p>
        <div class="tech-details">
          <strong>Key Applications:</strong> High-throughput screening, fragment-based drug discovery, competitive binding studies
        </div>
      </div>

      <div class="assay-card">
        <h3>Surface Plasmon Resonance (SPR)</h3>
        <p>Label-free technology for real-time monitoring of biomolecular interactions, providing kinetic and affinity data without requiring fluorescent tags.</p>
        <div class="tech-details">
          <strong>Key Applications:</strong> Kinetic parameter determination, epitope mapping, concentration analysis
        </div>
      </div>

      <div class="assay-card">
        <h3>Isothermal Titration Calorimetry (ITC)</h3>
        <p>Direct measurement of binding thermodynamics (ΔH, ΔS, ΔG) to characterize the energy landscape of molecular interactions.</p>
        <div class="tech-details">
          <strong>Key Applications:</strong> Mechanistic studies, thermodynamic profiling, stoichiometry determination
        </div>
      </div>
    </div>
  </div>

  <!-- 技术参数 -->
  <div class="section">
    <h2 class="section-title">Performance Characteristics</h2>
    <div class="tech-details">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
        <div>
          <strong>Affinity Range:</strong> pM to mM
        </div>
        <div>
          <strong>Throughput:</strong> 96/384/1536-well formats
        </div>
        <div>
          <strong>Sample Consumption:</strong> µL to mL scale
        </div>
        <div>
          <strong>Instrumentation:</strong> Biacore SPR, PHERAstar FS, MicroCal ITC200
        </div>
        <div>
          <strong>Automation:</strong> Liquid handling integration
        </div>
        <div>
          <strong>Data Output:</strong> Kd, kon, koff, ΔH, ΔS values
        </div>
      </div>
    </div>
  </div>

  <!-- 研究应用 -->
  <div class="section">
    <h2 class="section-title">Research Applications</h2>
    <ul class="application-list">
      <li>Screening of small molecule libraries against viral targets including DENV NS3 protease and influenza neuraminidase</li>
      <li>Characterization of antibody-antigen interactions for therapeutic antibody development</li>
      <li>Evaluation of peptide binding to cancer oncoproteins and signaling receptors</li>
      <li>Determination of compound specificity across related protein families to minimize off-target effects</li>
      <li>Analysis of protein-drug binding in the presence of resistance-conferring mutations</li>
      <li>Validation of computationally predicted binding interactions from AlphaFold3 models</li>
    </ul>
  </div>

  <!-- 合作号召 -->
  <div class="cta-section">
    <h3>Need Custom Binding Assay Development?</h3>
    <p>We offer collaborative assay development services tailored to specific therapeutic targets and research questions.</p>
    <a href="/contact/" class="cta-btn">Inquire About Collaboration</a>
  </div>
</div>