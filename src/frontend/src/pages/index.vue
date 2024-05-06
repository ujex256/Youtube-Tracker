<template>
  <div>
    <div class="pg-info">
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
      <img
        src="https://placehold.jp/500x350.png"
        alt="すごい紹介"
        class="info-img"
      />
    </div>
  </div>
</template>

<style scoped>
.pg-info {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 75vh;
  background-color: wheat;
}
.info-txt {
  position: relative;
  word-break: keep-all;
  max-width: 50vw;
  padding: 25px;
  width: fit-content;
  height: 75%;
  font-size: 1.25rem;
}
.info-catchphrase {
  font-size: 4rem;
}
.info-img {
  width: 30vw;
  height: auto;
}
.registerbtn {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}
</style>
