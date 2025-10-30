---
layout: default
title: Chemical Library
permalink: /chemlib/
---

<!-- 1. 页面样式 (CSS) -->
<style>
  .molecule-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 25px; padding: 20px; }
  .molecule-card { border: 1px solid #e0e0e0; border-radius: 12px; padding: 15px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out; }
  .molecule-card:hover { transform: translateY(-5px); box-shadow: 0 8px 12px rgba(0,0,0,0.1); }
  .molecule-card .structure { width: 100%; height: 180px; display: flex; align-items: center; justify-content: center; margin: 0 auto; }
  .molecule-card .structure svg { max-width: 100%; max-height: 100%; }
  .molecule-card p { margin-top: 15px; font-weight: 600; color: #333; font-family: monospace; font-size: 1.1em; }
</style>

<!-- 2. 页面内容 (HTML & Liquid) -->
<h1 style="text-align: center; margin-top: 20px;">Compound Library</h1>
<hr>
<div class="molecule-grid">
  {% for molecule in site.data.molecules %}
    <div class="molecule-card">
      <div class="structure" id="mol-{{ molecule.ID }}" data-smiles="{{ molecule.SMILES }}">
        <!-- JavaScript will draw the molecule here -->
      </div>
      <p>{{ molecule.ID }}</p>
    </div>
  {% endfor %}
</div>

<!-- 3. JavaScript部分 - 修复后的版本 -->

<!-- 从unpkg CDN加载RDKit.js库 -->
<script src="https://unpkg.com/@rdkit/rdkit/Code/MinimalLib/dist/RDKit_minimal.js"></script>

<!-- 使用RDKit绘制分子结构 -->
<script>
  // 定义绘图函数
  function drawMolecules(RDKit) {
    console.log("开始绘制分子结构...");
    
    const moleculeHolders = document.querySelectorAll('.structure[data-smiles]');
    console.log(`找到 ${moleculeHolders.length} 个分子需要绘制`);
    
    moleculeHolders.forEach((holder, index) => {
      const smiles = holder.dataset.smiles;
      if (smiles && smiles.trim() !== '') {
        try {
          const mol = RDKit.get_mol(smiles);
          if (mol && mol.is_valid()) {
            // 设置SVG大小为200x180
            const svg = mol.get_svg(200, 180); 
            holder.innerHTML = svg;
            mol.delete(); // 释放内存
            console.log(`成功绘制分子 ${index + 1}: ${smiles}`);
          } else {
            console.warn(`无效的SMILES: "${smiles}"`);
            holder.innerHTML = '<p style="color: red; font-size: 12px;">Invalid SMILES</p>';
          }
        } catch (e) {
          console.error(`绘制SMILES时出错: "${smiles}"`, e);
          holder.innerHTML = '<p style="color: red; font-size: 12px;">Render Error</p>';
        }
      }
    });
  }

  // 等待RDKit库完全加载后再初始化
  window.initRDKitModule().then(function (RDKit) {
    window.RDKit = RDKit;
    console.log('RDKit模块加载成功');
    
    // 检查DOM是否已加载
    if (document.readyState === 'loading') {
      // DOM还在加载中，等待加载完成
      document.addEventListener('DOMContentLoaded', function() {
        drawMolecules(RDKit);
      });
    } else {
      // DOM已经加载完成，直接绘制
      drawMolecules(RDKit);
    }
  }).catch((e) => {
    // 如果RDKit加载失败，显示错误信息
    console.error("RDKit.js初始化失败:", e);
    const grid = document.querySelector('.molecule-grid');
    if(grid) {
      grid.innerHTML = '<h2 style="color: red; text-align: center;">错误: 无法加载化学结构可视化工具</h2><p style="text-align: center;">请检查浏览器控制台获取详细信息</p>';
    }
  });
</script>
