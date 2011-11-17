<div id="${id}">
  % if pkg_description:
    <h3>Description</h3>
    <div class="package-description">${pkg_description}</div>
  % endif
  <div class="latest-build"></div>
  % if owner:
    <div class="package-owner"><a href="/people/?username=${owner}" moksha_url="dynamic">${owner}</a></div>
  % endif

</div>