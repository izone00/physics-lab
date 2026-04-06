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

### Research Projects

<style>
  .research-card {
    background-color: #f0f9ff;
    border-radius: 12px;
    overflow: hidden; /* For rounded image corners */
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
</style>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; margin-top: 1.5rem; margin-bottom: 2rem;">
  <!-- Theme 1 -->
  <div class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_01.png' | relative_url }}" alt="RHIC Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"/><path d="M20.2 20.2c2.04-2.03.02-7.36-4.52-11.9s-9.87-6.56-11.9-4.52c-2.04 2.03-.02 7.36 4.52 11.9s9.87 6.56 11.9 4.52z"/><path d="M15.8 15.8c2.04-2.03.02-7.36-4.52-11.9s-9.87-6.56-11.9-4.52c-2.04 2.03-.02 7.36 4.52 11.9s9.87 6.56 11.9 4.52z" transform="rotate(60 12 12)"/><path d="M15.8 15.8c2.04-2.03.02-7.36-4.52-11.9s-9.87-6.56-11.9-4.52c-2.04 2.03-.02 7.36 4.52 11.9s9.87 6.56 11.9 4.52z" transform="rotate(120 12 12)"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">PHENIX & sPHENIX at RHIC</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Exploring quark-gluon plasma and nuclear matter properties in relativistic heavy-ion collisions at Brookhaven National Laboratory.</span>
    </div>
  </div>
  <!-- Theme 2 -->
  <div class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_02.png' | relative_url }}" alt="LHC Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">ALICE at LHC</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Studying the properties of strongly interacting matter at the highest-ever energy densities using the ALICE detector at CERN.</span>
    </div>
  </div>
  <!-- Theme 3 -->
  <div class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_12.png' | relative_url }}" alt="RAON Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">LAMPS at RAON</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Investigating nuclear matter at extreme neutron-rich conditions using the rare isotope accelerator complex in Korea.</span>
    </div>
  </div>
  <!-- Theme 4 -->
  <div class="research-card">
    <img src="{{ '/assets/img/carousel/carousel_06.png' | relative_url }}" alt="EIC Research">
    <div class="research-card-content">
      <div style="color: #003876; margin-bottom: 0.6rem;">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="M2 12h2"/><path d="m4.93 19.07 1.41-1.41"/><path d="M12 22v-2"/><path d="m19.07 19.07-1.41-1.41"/><path d="M22 12h-2"/><path d="m19.07 4.93-1.41 1.41"/><path d="M15.93 15.93 12 12l3.93-3.93"/></svg>
      </div>
      <strong style="color: #003876; font-size: 1.25rem; display: block; margin-bottom: 1.2rem; font-family: 'Merriweather', serif;">ePIC at EIC</strong>
      <span style="font-size: 1rem; color: #334155; display: block; line-height: 1.6;">Probing the 3D structure of protons and nuclei through electron-ion collisions at the future Electron Ion Collider at BNL.</span>
    </div>
  </div>
</div>

---

### Lab Gallery

<div class="lab-carousel-wrap" style="position:relative; margin: 2rem 0; overflow:hidden; border-radius:8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);">
  <div class="lab-carousel-track" id="labCarousel" style="display:flex; transition: transform 0.5s ease;">
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_01.png' | relative_url }}" alt="Lab photo 1"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_02.png' | relative_url }}" alt="Lab photo 2"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_03.png' | relative_url }}" alt="Lab photo 3"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_04.png' | relative_url }}" alt="Lab photo 4"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_05.png' | relative_url }}" alt="Lab photo 5"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_06.png' | relative_url }}" alt="Lab photo 6"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_07.png' | relative_url }}" alt="Lab photo 7"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_08.png' | relative_url }}" alt="Lab photo 8"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_09.png' | relative_url }}" alt="Lab photo 9"  loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_10.png' | relative_url }}" alt="Lab photo 10" loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_11.png' | relative_url }}" alt="Lab photo 11" loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_12.png' | relative_url }}" alt="Lab photo 12" loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_13.png' | relative_url }}" alt="Lab photo 13" loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
    <div style="min-width:100%; height:420px; overflow:hidden;"><img src="{{ '/assets/img/carousel/carousel_14.png' | relative_url }}" alt="Lab photo 14" loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
  </div>
  <button onclick="labCarouselMove(-1)" aria-label="Previous" style="position:absolute;top:50%;left:12px;transform:translateY(-50%);background:rgba(0,0,0,0.45);color:#fff;border:none;border-radius:50%;width:40px;height:40px;font-size:1.4rem;cursor:pointer;z-index:10;">&#8249;</button>
  <button onclick="labCarouselMove(1)"  aria-label="Next"     style="position:absolute;top:50%;right:12px;transform:translateY(-50%);background:rgba(0,0,0,0.45);color:#fff;border:none;border-radius:50%;width:40px;height:40px;font-size:1.4rem;cursor:pointer;z-index:10;">&#8250;</button>
  <div id="labCarouselDots" style="position:absolute;bottom:12px;left:50%;transform:translateX(-50%);display:flex;gap:6px;z-index:10;"></div>
</div>

<script>
(function(){
  var track = document.getElementById('labCarousel');
  var dotsWrap = document.getElementById('labCarouselDots');
  var total = track ? track.children.length : 0;
  var current = 0, timer;
  function buildDots() {
    for (var i = 0; i < total; i++) {
      var d = document.createElement('button');
      d.style.cssText = 'width:8px;height:8px;border-radius:50%;border:none;cursor:pointer;padding:0;';
      d.setAttribute('data-idx', i);
      d.addEventListener('click', function(){ goTo(parseInt(this.getAttribute('data-idx'))); resetTimer(); });
      dotsWrap.appendChild(d);
    }
    updateDots();
  }
  function updateDots() {
    Array.from(dotsWrap.children).forEach(function(d, i){
      d.style.background = (i === current) ? '#fff' : 'rgba(255,255,255,0.45)';
    });
  }
  function goTo(n) {
    current = (n + total) % total;
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    updateDots();
  }
  window.labCarouselMove = function(dir){ goTo(current + dir); resetTimer(); };
  function resetTimer(){ clearInterval(timer); timer = setInterval(function(){ goTo(current + 1); }, 4500); }
  if (track && total > 0){ buildDots(); resetTimer(); }
})();
</script>
