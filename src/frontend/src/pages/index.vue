<template>
  <div>
    <div class="pg-info center">
      <BContainer>
        <BRow>
          <BCol class="center">
            <div class="info-txt">
              <h1 class="info-catchphrase">Hello, World</h1>
              <span>Youtube, NicoNicoなど</span>
              <br />
              <span>様々なプラットフォームの動画の</span>
              <br />
              <span>再生回数や高評価数などを分析します。</span>
              <div class="d-grid gap-2">
                <BButton
                  pill
                  variant="primary"
                  class="registerbtn mx-3 my-4 px-4"
                >
                  <Icon
                    name="ant-design:video-camera-add-outlined"
                    size="1.5rem"
                  />
                  自分の動画を登録してみる
                </BButton>
              </div>
            </div>
          </BCol>
          <BCol class="center">
            <img
              src="https://placehold.jp/500x350.png"
              alt="すごい紹介"
              class="info-img"
            />
          </BCol>
        </BRow>
      </BContainer>
    </div>
    <div class="search text-center">
      <h1 class="display-3">検索してみる</h1>
      <BContainer fluid class="p-0">
        <BForm class="d-flex align-items-center flex-column row-gap-4">
          <BInputGroup class="display-input rounded-pill">
            <BDropdown
              text="動画サイト"
              toggle-class="px-3 rounded-5 rounded-end-0"
            >
              <DropIconItem name="logos:youtube-icon">Youtube</DropIconItem>
              <DropIconItem name="arcticons:niconico">NicoNico</DropIconItem>
            </BDropdown>
            <BFormInput type="url" placeholder="動画URL" />
            <BButton
              class="d-none d-md-block rounded-5 rounded-start-0"
              variant="primary"
            >
              <Icon name="mingcute:search-3-line" size="1.7em" class="mx-2" />
            </BButton>
          </BInputGroup>
          <BButton class="d-md-none col-4" variant="primary">
            <Icon name="mingcute:search-3-line" size="1.7em" class="mx-2" />
          </BButton>
        </BForm>
      </BContainer>
      <div class="my-5 d-flex align-items-center flex-column">
        <img
            src="https://placehold.jp/600x350.png"
            alt="グラフとか"
            class="info-img"
        />
        <h1>できること</h1>
        <div>
          <BCard>
            <BCardTitle>見やすいグラフで直感的に見れる</BCardTitle>
            <BCardText>{{ "こんにちは".repeat(80) }}</BCardText>
          </BCard>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.pg-info {
  padding: 7.5%;
  background-color: wheat;
}
.info-txt {
  word-break: keep-all;
  width: fit-content;
  font-size: clamp(1.125rem, 1.031rem + 0.47vw, 1.5rem);
}
.info-catchphrase {
  white-space: nowrap;
  font-size: clamp(3rem, 2.625rem + 1.88vw, 4.5rem);
}
.info-img {
  margin: 10px;
  min-width: 25vw;
  max-width: 90%;
}
.registerbtn {
  padding: 0.8rem 0;
  font-size: clamp(1rem, 0.938rem + 0.31vw, 1.2rem);
}
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

.search {
  padding: 5%;
  background-color: lightskyblue;
}
.display-input {
  box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.35);
  height: 56px;
  max-width: 800px;
  transition: all 0.3s;
}
.display-input:focus-within {
  box-shadow: 0px 10px 10px 0px rgba(0, 0, 0, 0.35);
}
.display-input * {
  font-size: 1.1rem;
}
</style>
