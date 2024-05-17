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
                <BButton pill variant="primary" class="registerbtn mx-3 my-4 px-4">
                  <Icon name="ant-design:video-camera-add-outlined" size="1.5rem" />
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
    <div class="search">

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
  min-width: 32vw;
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
</style>
