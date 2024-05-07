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
                <BButton pill variant="primary" class="registerbtn m-3 px-5">
                  <Icon name="ant-design:video-camera-add-outlined" size="1.5em" />
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
  </div>
</template>

<style scoped>
.pg-info {
  height: 75vh;
  background-color: wheat;
}
.info-txt {
  word-break: keep-all;
  /* padding: 25px;
  max-width: 8vw; */
  width: fit-content;
  font-size: clamp(1.125rem, 1.03rem + 0.48vw, 1.625rem);
}
.info-catchphrase {
  font-size: clamp(3.5rem, 3.274rem + 1.13vw, 4.688rem);
}
.info-img {
  width: 30vw;
  height: auto;
}
.registerbtn {
  padding: 0.75rem 0;
}
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
