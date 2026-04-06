---
layout: about
title: Home
permalink: /
subtitle: Department of Physics, Yonsei University
nav: false
nav_order: 1

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 5

latest_posts:
  enabled: false
---

Welcome to the **Nuclear Physics Laboratory** at Yonsei University. Strong interaction is one of the four fundamental interactions, and it binds quarks inside a nucleon and nucleons inside a nucleus. We are exploring nuclear matters at various temperature and density to understand the properties emerging from the strong interaction. Research in the lab spans a wide range of activity on particle detectors, software, data analysis, simulation, and model.

We are looking for new members! If you are interested, please <a href="mailto:contact@yonsei.ac.kr">contact us</a>.

### <a href="{{ '/projects/' | relative_url }}" style="color: inherit; text-decoration: none;">Research Projects &rsaquo;</a>

<style>
  .research-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }
  .research-card {
    background-color: #f0f9ff;
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
  }
  .research-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  }
  .research-card img {
    width: 100%;
    aspect-ratio: 16/9;
    object-fit: cover;
    filter: grayscale(100%);
    transition: filter 0.4s ease;
  }
  .research-card:hover img {
    filter: grayscale(0%);
  }
  .research-card-content {
    padding: 2rem;
  }

  /* Responsive Swipe for Mobile */
  @media (max-width: 768px) {
    .research-grid {
      display: flex;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      gap: 1rem;
      padding: 0.5rem 1rem 1.5rem 1rem;
      margin-left: -1rem;
      margin-right: -1rem;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: thin;
      scrollbar-color: #cbd5e1 transparent;
    }
    .research-grid::-webkit-scrollbar {
      height: 4px;
    }
    .research-grid::-webkit-scrollbar-thumb {
      background: #cbd5e1;
      border-radius: 10px;
    }
    .research-card {
      min-width: 85%;
      scroll-snap-align: center;
    }
  }
</style>

<div class="research-grid">
  <!-- Theme 1 -->
  <a href="{{ '/projects/' | relative_url }}" class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_01.png' | relative_url }}" alt="RHIC Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"/><path d="M20.2 20.2c2.04-2.03.02-7.36-4.52-11.9s-9.87-6.56-11.9-4.52c-2.04 2.03-.02 7.36 4.52 11.9s9.87 6.56 11.9 4.52z"/><path d="M15.8 15.8c2.04-2.03.02-7.36-4.52-11.9s-9.87-6.56-11.9-4.52c-2.04 2.03-.02 7.36 4.52 11.9s9.87 6.56 11.9 4.52z" transform="rotate(60 12 12)"/><path d="M15.8 15.8c2.04-2.03.02-7.36-4.52-11.9s-9.87-6.56-11.9-4.52c-2.04 2.03-.02 7.36 4.52 11.9s9.87 6.56 11.9 4.52z" transform="rotate(120 12 12)"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">PHENIX & sPHENIX at RHIC</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Exploring quark-gluon plasma and nuclear matter properties in relativistic heavy-ion collisions at Brookhaven National Laboratory.</span>
    </div>
  </a>
  <!-- Theme 2 -->
  <a href="{{ '/projects/' | relative_url }}" class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_02.png' | relative_url }}" alt="LHC Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">ALICE at LHC</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Studying the properties of strongly interacting matter at the highest-ever energy densities using the ALICE detector at CERN.</span>
    </div>
  </a>
  <!-- Theme 3 -->
  <a href="{{ '/projects/' | relative_url }}" class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_12.png' | relative_url }}" alt="RAON Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">LAMPS at RAON</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Investigating nuclear matter at extreme neutron-rich conditions using the rare isotope accelerator complex in Korea.</span>
    </div>
  </a>
  <!-- Theme 4 -->
  <a href="{{ '/projects/' | relative_url }}" class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_06.png' | relative_url }}" alt="EIC Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="M2 12h2"/><path d="m4.93 19.07 1.41-1.41"/><path d="M12 22v-2"/><path d="m19.07 19.07-1.41-1.41"/><path d="M22 12h-2"/><path d="m19.07 4.93-1.41 1.41"/><path d="M15.93 15.93 12 12l3.93-3.93"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">ePIC at EIC</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Probing the 3D structure of protons and nuclei through electron-ion collisions at the future Electron Ion Collider at BNL.</span>
    </div>
  </a>
</div>

---

### <a href="{{ '/gallery/' | relative_url }}" style="color: inherit; text-decoration: none;">Lab Gallery &rsaquo;</a>

<div class="gallery-preview" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 1.5rem 0;">
  {% for i in (1..6) %}
    {% capture num %}{% if i < 10 %}0{{ i }}{% else %}{{ i }}{% endif %}{% endcapture %}
    <a href="{{ '/gallery/' | relative_url }}" style="display: block; border-radius: 8px; overflow: hidden; height: 180px;">
      <img src="{{ '/assets/img/carousel/carousel_' | append: num | append: '.png' | relative_url }}" alt="Lab photo preview" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
    </a>
  {% endfor %}
</div>

<div style="text-align: right; margin-bottom: 3rem;">
  <a href="{{ '/gallery/' | relative_url }}" class="btn btn-sm btn-outline-primary" style="border-radius: 20px; padding: 0.5rem 1.5rem;">See All Lab Photos &rarr;</a>
</div>
