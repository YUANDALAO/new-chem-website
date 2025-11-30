---
layout: default
title: Research - Chemical Assays
permalink: /research/chemical-assays/
---
<div class="container" style="padding: 2rem 0;">
<!-- 新增移动端顶部间距适配（与其他研究页面保持样式统一） -->
  <style>
    @media (max-width: 768px) {
      .container {
        padding-top: 4rem !important; /* 根据网站导航栏实际高度调整，确保移动端显示完整 */
      }
    }
  </style>

  <!-- 页面主标题与核心介绍 -->
  <h1>Chemical Assays</h1>
  <hr>
  <p style="font-size: 1.1em; line-height: 1.6;">
    Our research leverages advanced chemical assay development to bridge synthetic chemistry and biological validation, providing quantitative insights into molecular interactions, enzyme function, and metabolite dynamics. These assays serve as critical tools for drug target validation, lead compound screening, and mechanism-of-action studies—supporting our broader research goals in antiviral and therapeutic development.
  </p>

  <!-- 整合主research页面对应的Chemical Assay Section板块（超链接完全匹配） -->
  <div class="research-section" style="margin-top: 2.5rem;">
    <div class="section-header">
      <h2>Chemical Assay Types</h2>
    </div>
    <div class="research-grid">
      <a href="{{ '/research/chemical-assays/enzymatic/' | relative_url }}" class="research-card">
        <h3>Enzymatic Activity Assays</h3>
        <p>Development of high-throughput chemical assays to measure enzyme kinetics, inhibition constants, and substrate specificity for drug target validation.</p>
        <span class="read-more-link">Learn More</span>
      </a>

      <a href="{{ '/research/chemical-assays/binding/' | relative_url }}" class="research-card">
        <h3>Molecular Binding Assays</h3>
        <p>Design of fluorescence-based and SPR-based chemical assays to quantify biomolecular interactions between small molecules and target proteins.</p>
        <span class="read-more-link">Explore Methods</span>
      </a>

      <a href="{{ '/research/chemical-assays/metabolite/' | relative_url }}" class="research-card">
        <h3>Metabolite Detection Assays</h3>
        <p>Development of LC-MS/MS based chemical assays for sensitive quantification of endogenous metabolites in biological samples.</p>
        <span class="read-more-link">View Protocols</span>
      </a>
    </div>
  </div>
</div>