# 沼って。 LP

TikTok LIVE ライバー事務所「沼って。」のランディングページ。

- 公開URL: https://numatte.github.io/
- `index.html` 1ファイル＋`assets/`（写真）で動く静的サイト。GitHub Pages（main ブランチ直下）で公開している
- 写真は `python build_images.py <numatte-lp.pdf>` で、元のPDFから取り出してWeb用に軽くしたもの（ヒーローの `assets/hero-taishi-full.jpg` だけは、本人からもらった縦長の元写真）
- ヒーローはPCだと「左に文字・右に写真」、スマホだと「写真の下に文字」で、どちらも写真を切らずに全体を見せる
- 直したら main に push すると、1〜2分でサイトに反映される
- **LINE公式アカウントはまだないので、LINEボタンは「準備中」表示にしている**（2026-11-04）。できたら `index.html` の「LINE準備中」コメント3か所に従って、友だち追加URLのボタンとスマホ下の固定ボタンに戻す
