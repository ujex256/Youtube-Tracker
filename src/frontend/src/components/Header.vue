<template>
  <header data-bs-theme="dark">
    <BNavbar class="hd-nav shadow p-3" container="xl">
      <span class="navbar-brand mb-0 h1" style="font-size: 1.4rem;">
        SNAME
      </span>
      <div class="hd-btns">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Main3</a>
          </li>
          <a class="nav-item" href="#">
            <BButton variant="outline-primary">Login</BButton>
          </a>
        </ul>
      </div>
    </BNavbar>
  </header>
</template>

<style scoped>
.hd-nav {
  padding-left: 5%;
  padding-right: 5%;
  background-color: rgb(137, 195, 235);
}
</style>
