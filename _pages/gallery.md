---
layout: page
title: Gallery
permalink: /gallery/
description: Visual highlights from our laboratory and experiments.
nav: true
nav_order: 7
---

Welcome to our laboratory gallery. Here we share highlights of our research facilities, experiment setups, and team activities. Click on any image to view it in full size.

<style>
  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin: 3rem 0;
  }
  .gallery-item {
    position: relative;
    border-radius: 12px;
    overflow: hidden;
    aspect-ratio: 4/3;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    cursor: pointer;
  }
  .gallery-item:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
  }
  .gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s ease;
  }
  .gallery-item:hover img {
    transform: scale(1.1);
  }
  .gallery-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, transparent 60%, rgba(0, 56, 118, 0.6));
    opacity: 0;
    transition: opacity 0.3s ease;
    display: flex;
    align-items: flex-end;
    padding: 20px;
  }
  .gallery-item:hover .gallery-overlay {
    opacity: 1;
  }
  .gallery-text {
    color: #fff;
    font-size: 0.9rem;
    font-weight: 500;
  }
</style>

<div class="gallery-grid">
  {% for i in (1..14) %}
    {% capture num %}{% if i < 10 %}0{{ i }}{% else %}{{ i }}{% endif %}{% endcapture %}
    {% capture img_url %}/assets/img/carousel/carousel_{{ num }}.png{% endcapture %}
    <a href="{{ img_url | relative_url }}" class="venobox gallery-item" data-gall="labGallery" data-title="Laboratory Highlight {{ i }}">
      <img src="{{ img_url | relative_url }}" alt="Lab photo {{ i }}" loading="lazy">
      <div class="gallery-overlay">
        <span class="gallery-text">Lab View #{{ i }}</span>
      </div>
    </a>
  {% endfor %}
</div>
