---
type: index
title: 检索索引（自动生成）
description: 全部概念页的紧凑清单，agent 优先读本文件定位，再下钻。
---

# 检索索引

> 自动生成，共 **180** 个概念页。**请勿手工编辑**——由 `tools/build_index.py` 产出。
> 完整数据（含关键词与出/入链）见 `graph.json`。

## 用法（给 agent）

1. 在本文件按 `type` / 标签 / 关键词定位候选页
2. 只读候选页，不要遍历全部 index.md
3. 需要关系数据（谁引用了谁）时读 `graph.json`

## Color Palette（5）

- [冷调金属（Chrome Cool）](../atlas/color/chrome-cool-palette.md) — 铬银、冰蓝、亮黑、纯白构成的冷峻科技配色。
- [霓虹撞色（Neon Clash）](../atlas/color/neon-clash-palette.md) — 热粉、电光蓝、酸绿在深色底上高饱和对撞，视觉侵略性强。
- [梦幻马卡龙（Pastel Candy）](../atlas/color/pastel-candy-palette.md) — 婴儿粉、婴儿蓝、淡紫、薄荷构成的柔和甜美配色。
- [视觉系·黑白冷调（Visual Kei Monochrome）](../atlas/color/visual-kei-monochrome.md) — 视觉系的骨架配色——纯黑、石膏白、银灰三色构成的高对比冷调，Kote-kei 的标准色板。
- [暖调 DV · 古铜脏金（Warm DV Bronze）](../atlas/color/warm-dv-bronze-palette.md) — 橙粉、古铜、脏金、焦橙构成的暖调配色，像老 DV 磁带与千禧杂志内页的夕照色调。

## Guide（8）

- [图像资产层规范](../guides/image-assets.md) — 本地图像资产的存放、命名、绑定与检索约定，解决"审美资产依赖外部 CDN"的结构性风险。
- [图片生成规范](../guides/image-generation.md) — 将风格配方或临时选择组装为图像模型 prompt、负向词与参数的规范。
- [原料编译管道](../guides/ingestion.md) — 将 raw/ 中的审美书籍、杂志、扫描件、文章编译为 atlas/ 结构化概念的流程。
- [维护规范](../guides/maintenance.md) — 资产库命名、粒度、元数据、索引、日志、生命周期与配方版本规则。
- [新建风格包规范](../guides/new-style-pack.md) — 如何为本库新增一个风格运动、子风格或风格家族，含完整 checklist 与质量门槛。
- [配方 schema 规范](../guides/recipe-schema.md) — 配方双表示约定（Markdown 给人读 + YAML 给 agent 读）、字段定义与校验规则。
- [风格探索协议](../guides/style-exploration.md) — Agent 基于资产库与用户共同探索、收敛并沉淀视觉风格的对话流程。
- [视频生成规范](../guides/video-generation.md) — 将图片与风格配方组装为视频生成 prompt（运镜/动作/节奏/转场/声音）的规范。

## Motion Element（22）

- [抓拍说笑（Candid Laugh & Talk）](../atlas/motion/candid-laugh.md) — 像没注意到镜头一样自然说笑、捂嘴、歪头，DV 真实感的核心表演。
- [舞蹈律动（Dance / Groove）](../atlas/motion/dance-routine.md) — 随节拍起舞或上半身律动，偶像与派对场景的高能动作。
- [数据 Moshing（Datamosh）](../atlas/motion/datamosh.md) — 利用视频压缩错误产生的画面融化、拖尾与撕裂，数字破坏美学。
- [跟拍平移（Dolly / Tracking）](../atlas/motion/dolly-tracking.md) — 镜头平滑横向移动或跟随主体行进，稳定流畅，电影感。
- [斜角漂移（Dutch Drift）](../atlas/motion/dutch-drift.md) — 倾斜构图并缓慢漂移，制造不安、迷幻或先锋时尚感。
- [快切高能（Fast Montage）](../atlas/motion/fast-montage.md) — 短镜头快速组接、信息密集、节奏强烈，适合高能与潮流内容。
- [闪白/遮挡转场（Flash Frame）](../atlas/motion/flash-frame.md) — 用闪白、闪光灯、物体掠过遮挡完成切换，干脆且有节奏。
- [漂浮粒子（Floating Particles）](../atlas/motion/floating-particles.md) — 空气中漂浮的尘埃、亮片、光点或泡泡，在光下闪烁，增强梦幻层次。
- [拖影/动态模糊（Frame-Blend Ghost）](../atlas/motion/frame-blend-ghost.md) — 帧混合产生的重影、拖尾与慢速快门模糊，梦幻或迷幻。
- [故障转场（Glitch Cut）](../atlas/motion/glitch-cut.md) — 以数字故障、画面撕裂或信号中断完成镜头切换，Retro-Future 标志。
- [撩发回眸（Hair Flip & Turn）](../atlas/motion/hair-flip-turn.md) — 主体撩起头发或回头看向镜头，发丝甩出弧线，是 MV 最经典的人物动作。
- [手持浮动（Handheld Sway）](../atlas/motion/handheld-sway.md) — 模仿手持摄像机的轻微晃动与呼吸感，像真实在场的抓拍，DV 风格核心运镜。
- [光流扫过（Light Sweep）](../atlas/motion/light-sweep.md) — 光斑、反射或霓虹色彩在画面与人物表面缓慢流动。
- [慢速梦幻（Slow Dream Pacing）](../atlas/motion/slow-dream.md) — 长镜头、慢动作、留白与舒缓节奏，让观众沉浸在氛围里。
- [缓慢环绕（Slow Orbit）](../atlas/motion/slow-orbit.md) — 镜头围绕主体缓慢弧形环绕，展示立体感与闪亮轮廓。
- [缓慢推进（Slow Push-In）](../atlas/motion/slow-push-in.md) — 镜头向主体极缓慢推近，制造凝视、沉浸与情绪收紧。
- [舞台表演动态（Stage Performance Motion）](../atlas/motion/stage-performance-motion.md) — 视觉系的视频动态语汇——甩头、抬手、转身、布料飞扬等带有强烈表演性的动作。
- [频闪（Strobe Flash）](../atlas/motion/strobe.md) — 高频明暗闪烁或闪光灯连打，制造强烈节奏与冲击。
- [磁带跟踪故障（Tape Tracking）](../atlas/motion/tape-tracking.md) — VHS 磁迹错位产生的横向条纹、画面滚动与丢帧。
- [走向镜头（Walk Toward Camera）](../atlas/motion/walk-toward.md) — 主体迎面走来，步伐自信，背景后退，强势且有气场。
- [急推变焦（Whip Zoom）](../atlas/motion/whip-zoom.md) — 千禧 DV 标志性的突然数码变焦，快速推近脸部或细节，带粗糙与即兴感。
- [风吹头发与衣物（Wind Motion）](../atlas/motion/wind-hair-fabric.md) — 微风或风扇吹动发丝、开衫、薄纱与配饰，让画面「活」起来。

## Raw Source（2）

- [<原料标题>](../raw/_template-source.md) — <一句话说明这份原料是什么>
- [千禧年低多边形 3D 短片合集（4 部，PS1/PS2-era 风格）](../raw/videos/_source.md) — 4 部日系 2000s 复古 3D / 动漫短片，覆盖 JK 校园日常、地下通道、走廊监控、食堂、教室场景。

## Reference（11）

- [Dior by John Galliano](../references/brands/dior-galliano.md) — Galliano 执掌的 Christian Dior（1997–2011），千禧高定的浪漫、流浪与华丽混搭。
- [Juicy Couture](../references/brands/juicy-couture.md) — 美国品牌，以彩色丝绒运动套装定义千禧名流「运动奢华」休闲风。
- [Louis Vuitton × Murakami](../references/brands/louis-vuitton-murakami.md) — 2003 年起 Louis Vuitton 与村上隆联名，彩色/樱花 monogram 把高定、街头与御宅文化融合。
- [Von Dutch](../references/brands/von-dutch.md) — 以卡车帽与 Kustom Kulture 美学闻名的街头品牌，千禧 logomania 代表。
- [David LaChapelle（大卫·拉夏培尔）](../references/creators/david-lachapelle.md) — 高饱和超现实千禧商业摄影师。
- [时代：1990s 末–2000s 初（Late 90s–Early 00s）](../references/eras/late-1990s-early-2000s.md) — 千禧年之交的技术、媒介与流行文化背景。
- [蝴蝶母题（Butterfly Motif）](../references/iconography/butterfly-motif.md) — Y2K 最具代表性的轻盈符号。
- [火焰母题（Flame Motif）](../references/iconography/flame-motif.md) — 横跨甜酷与街头的热情/危险符号。
- [爱心母题（Heart Motif）](../references/iconography/heart-motif.md) — 浪漫甜美的核心符号，常带光泽或火焰变体。
- [千禧年 MV 合集（Millennium Music Videos）](../references/works/millennium-mvs.md) — 塑造 Y2K 视觉的欧美与日韩标志性 MV。
- [《黑客帝国》（The Matrix, 1999）](../references/works/the-matrix.md) — Cyber Metal 子风格的电影视觉锚点。

## Style Movement（3）

- [复古游戏 CG（Retro Game CG · PS1/PS2-era Low-Poly 3D）](../atlas/taxonomy/movements/retro-game-cg.md) — 1997–2006 年 PS1/PS2 世代游戏画面风格的 3D 渲染美学——低多边形、低分辨率贴图、vertex wobble、固定视角，延伸至同人 CG 与虚拟主播圈。
- [Visual Kei · 日系视觉系](../atlas/taxonomy/movements/visual-kei.md) — 1980s 中起于日本摇滚场景的视觉化美学家族，以戏剧化妆容、极端发型与华丽服装为核心，90s 末–00s 初为黄金期。
- [Y2K · 千禧年风格](../atlas/taxonomy/movements/y2k.md) — 约1997–2006千禧之交的乐观未来主义风格，含四大子风格。

## Style Recipe（3）

- [PS2 低多边形 JK 校园日常（PS2 Low-Poly JK Slice-of-Life）](../recipes/ps2-lowpoly-jk-slice-of-life.md) — 2000s PS1/PS2 游戏渲染风格的低多边形 JK 校园日常——块状头发、贴图五官、走廊/食堂/地下通道场景，含图/视频双 prompt。
- [Visual Kei · Kote-kei 冷黑肖像（Cold Black Kote-kei Portrait）](../recipes/visual-kei-kote-cold-black.md) — 全黑西装、石膏白妆、尖刺立发的经典日系视觉系配方，强单点硬光与高对比质感，含图/视频双 prompt。
- [Y2K · 暖调 DV 千禧偶像（Warm DV Millennium Idol）](../recipes/y2k-warm-dv-idol.md) — 橙粉/古铜/脏金暖调、老DV与杂志质感的亚洲偶像少女配方，含图/视频双prompt。

## Style Substyle（11）

- [Angura / 暗黑哥特系（アングラ系）](../atlas/taxonomy/movements/visual-kei-angura.md) — 视觉系最戏剧化、艺术性最强的分支——华美颓废的欧风哥特与和风混搭，病态贵族感。
- [Kirakira / 华丽系（キラキラ系）](../atlas/taxonomy/movements/visual-kei-kirakira.md) — 视觉系的极致炫耀分支——亮片、水钻、羽毛、金属光泽，追求舞台级的炫目奢靡。
- [Kote-kei · 古典系（コテ系）](../atlas/taxonomy/movements/visual-kei-kote-kei.md) — 视觉系最正统的分支——全黑西装、极白妆容、尖刺立发，冷峻锐利的攻击性美学。
- [Oshare-kei · 御洒落系（お洒落系）](../atlas/taxonomy/movements/visual-kei-oshare-kei.md) — 视觉系的轻量甜美分支——彩色头发、糖果色穿搭、明快亲和，是视觉系与 Y2K 流行文化的交叉点。
- [Cyber Goth · 赛博哥特（冷黑金属亚文化）](../atlas/taxonomy/movements/y2k-cyber-goth.md) — Y2K 与哥特、工业、锐舞文化交汇的冷黑分支——全黑、PVC、护目镜、赛博义体感，去甜味的暗黑科技。
- [Cyber Metal · 赛博金属系](../atlas/taxonomy/movements/y2k-cyber-metal.md) — Y2K 的冷峻科技分支：液态金属、镀铬表面、乳胶与 PVC 紧身轮廓，受《黑客帝国》、太空时代时装与千禧年数字界面启发，呈现光滑、反光、近乎无机质的未来感。
- [Grunge Glam · 垃圾华丽系](../atlas/taxonomy/movements/y2k-grunge-glam.md) — Y2K 的叛逆分支：emo/朋克/滑板文化与华丽金属装饰对撞——做旧皮革、渔网、铆钉、脏粉与古铜，在颓废和闪亮之间制造张力。
- [里原宿 / 涩谷系（Harajuku & Shibuya Street）](../atlas/taxonomy/movements/y2k-harajuku-shibuya.md) — 日本街头亚文化分支——Decora 堆叠、Gyaru 辣妹、涩谷休闲，色彩与配饰密度极高，是日系 Y2K 与视觉系的交汇地带。
- [McBling · 奢华浮夸（炫富美学）](../atlas/taxonomy/movements/y2k-mcbling.md) — 2000s 嘻哈与名媛文化驱动的炫富分支——水钻、皮草、镀铬、Logo 狂热，把"贵"字写在身上。
- [Retro Future · 复古未来主义](../atlas/taxonomy/movements/y2k-retro-future.md) — Y2K 的低保真数字分支：早期 3D 渲染、低多边形、像素图形、Windows 98 界面、VHS/DV 影像，以今天的眼光怀旧千禧年人们想象中的数字世界。
- [Sweet Candy · 千禧甜酷系](../atlas/taxonomy/movements/y2k-sweet-candy.md) — Y2K 的甜辣少女分支：马卡龙粉蓝紫、亮片、蝴蝶与爱心符号，融合娃娃感与街头辣妹态度，是偶像工业与 McBling 消费文化的甜美产物。

## Unknown（1）

- [AGENTS.md](../AGENTS.md) — 原子元素   ──组合──▶  子风格   ──锁定──▶  配方

## Visual Element（109）

- [印花方巾（Bandana）](../atlas/accessories/bandana.md) — 佩斯利印花棉质方巾，系于颈、头、腕或包袋，街头与嘻哈元素。
- [肚链（Belly Chain）](../atlas/accessories/belly-chain.md) — 环绕腰腹、垂在小腹或髋骨的细链，强调露腰造型，是千禧辣妹标志。
- [身体亮片/水钻贴（Body Glitter）](../atlas/accessories/body-glitter.md) — 涂抹或贴在肩颈、锁骨、手臂、腰腹的闪粉与水钻，让皮肤本身成为装饰。
- [Choker（贴颈项链）](../atlas/accessories/choker.md) — 紧贴脖颈的短项链，材质从丝绒、珍珠到水钻、纹身印花皆有，Y2K 各子风格通用。
- [发饰（Hair Accessories）](../atlas/accessories/hair-accessories.md) — 蝴蝶夹、鸭嘴夹、大肠圈、缎带发带等千禧发饰聚合。
- [圈形耳环（Hoop Earrings）](../atlas/accessories/hoop-earrings.md) — 大小不一的金属圆环耳环，嘻哈与名流造型常见，大号最具年代感。
- [徽标腰带（Logo Belt）](../atlas/accessories/logo-belt.md) — 带醒目品牌字母扣、铆钉或水钻的腰带，系在低腰裤/裙上，强调腰线与 logo 狂热。
- [迷你包（Mini Bag）](../atlas/accessories/mini-bag.md) — 腋下或手持的极小包袋，金属、漆皮、徽标款，容量让位造型。
- [水钻叠戴首饰（Rhinestone Jewelry Set）](../atlas/accessories/rhinestone-jewelry-set.md) — 成组、多层叠戴的水钻/水晶首饰（项链、手链、戒指、耳环），制造密集闪亮。
- [包裹式墨镜（Wrap Sunglasses）](../atlas/accessories/wrap-sunglasses.md) — 流线包裹、窄框或无边、镜面镜片的运动感墨镜，千禧未来感标志。
- [欧陆舞曲（Europop Dance Anthem）](../atlas/audio/europop-dance-anthem.md) — 千禧年明亮欧陆舞曲/Teen Pop 风格。
- [R&B 抒情（R&B Ballad）](../atlas/audio/rnb-ballad.md) — 千禧年丝滑 R&B 慢板风格。
- [鱼眼镜头（Fisheye Lens）](../atlas/camera/fisheye-lens.md) — 超广角、桶形畸变、球面夸张透视，千禧滑板/派对/偶像写真的标志镜头。
- [监控视角 / CCTV 高角度（Security Camera / CCTV Angle）](../atlas/camera/security-camera-cctv.md) — 走廊尽头、天花板角落的固定高角度监控摄像头视角——画面带 surveillance 感，常与 bounding box、时间码叠层搭配。
- [第三人称游戏视角（Third-Person Game Camera）](../atlas/camera/third-person-game-camera.md) — 跟随主体背后或越肩的 3D 游戏视角——镜头随主体移动，观众看到主体后脑勺与前方场景，是 PS1/PS2 游戏与同人 CG 的默认运镜。
- [去现代数码感（Anti-Modern-Digital / Period Authenticity）](../atlas/grade/anti-modern-digital.md) — 对抗生成模型"默认输出当代高清数码照片"倾向的负向控制元素——年代真实性的强制手段。
- [交叉冲洗 / 褪色（Cross-Processing）](../atlas/grade/cross-processing.md) — 胶片以错误药水冲洗产生的偏色、高对比与不饱和褪色，复古艺术质感。
- [后期叠层（Digital Overlays）](../atlas/grade/digital-overlays.md) — 时间码、REC 标识、贴纸、边框、UI 元素、星形闪光、监控 bounding box、双语字幕等后期图形叠层。
- [胶片颗粒（Film Grain）](../atlas/grade/film-grain.md) — 胶片介质的银盐颗粒与自然宽容度，比数码更有呼吸感。
- [高对比戏剧质感（High-Contrast Dramatic Grade）](../atlas/grade/high-contrast-grade.md) — 视觉系的画面质感——深黑压暗、高光锐利、整体去饱和或强偏色，去掉一切生活感。
- [光晕 / 柔焦（Lens Flare & Haze）](../atlas/grade/lens-flare-haze.md) — 镜头眩光、光晕、雾化与柔焦，制造梦幻和神圣感。
- [漏光（Light Leak）](../atlas/grade/light-leak.md) — 胶片相机漏光在画面边缘形成的暖色光斑，随机而复古。
- [低多边形 3D 渲染（Low-Poly 3D Render）](../atlas/grade/low-poly-3d-render.md) — PS1/PS2 世代游戏实时渲染的视觉特征——可见三角面、低分辨率贴图、vertex wobble、简单光照，是 Retro Game CG 风格运动的核心介质。
- [千禧杂志片调色（Magazine Flash Grade）](../atlas/grade/magazine-flash-grade.md) — 高饱和、闪光灯直打、肤色暖亮、对比明快的杂志内页/封面调色。
- [PS2 FMV 预渲染质感（PS2 FMV Grade / Pre-rendered CG）](../atlas/grade/ps2-fmv-grade.md) — PS2 世代游戏预渲染过场动画（FMV / OP / ED）的画面质感——比实时渲染精细但仍保留 2000s CG 的渲染限制痕迹，介于低模与当代 3D 之间。
- [VHS / DV 磁带质感（VHS-DV Texture）](../atlas/grade/vhs-dv-texture.md) — 家用录像带与数码摄像机的影像特征：噪点、扫描线、色差、跟踪条、低分辨率与时间码。
- [块状挑染（Chunky Highlights）](../atlas/hair/chunky-highlights.md) — 用粗大发片做高对比度的高光挑染，是千禧年最具辨识度的染发方式，强调光泽与层次。
- [锡纸/玉米烫（Crimped Hair）](../atlas/hair/crimped-hair.md) — 用夹板压出细密波浪纹理（玉米须/锡纸烫），制造巨大蓬松体积与纹理光泽。
- [遮眼刘海（Eye-Covering Bangs）](../atlas/hair/eye-covering-bangs.md) — 长刘海完全或部分遮盖眼睛的发型，制造神秘、阴郁、不可接近的视觉系气质。
- [脸际高光碎发（Face-Framing Pieces）](../atlas/hair/face-framing-highlights.md) — 脸周细碎、更亮的发丝（类似蝴蝶剪/层次剪），修饰脸型并制造蓬松灵动的轮廓。
- [离子烫中分长直（Pin-Straight Ionic）](../atlas/hair/pin-straight-ionic.md) — 离子烫打造的中分/偏分超亮泽长直发，垂顺服帖，是千禧偶像剧女主标配。
- [侧马尾（Side Ponytail）](../atlas/hair/side-ponytail.md) — 在耳侧高位或低位扎起的马尾，俏皮复古，常留蓬松碎发与高光。
- [双丸子/面包头（Space Buns）](../atlas/hair/space-buns.md) — 头顶两侧盘起的圆发髻（面包头），俏皮太空感，常留碎发与挑染。
- [尖刺立发（Spiky Styled Hair）](../atlas/hair/spiky-styled-hair.md) — 用大量定型剂把头发做成放射状、有方向的尖刺结构，是 Kote-kei 视觉系最具辨识度的发型符号。
- [闪光灯直打（Direct On-Camera Flash）](../atlas/lighting/direct-flash.md) — 机顶闪光灯正面硬光，背景压暗、皮肤油亮、红眼与硬阴影，千禧派对与杂志快照标志。
- [强单点光（Dramatic Single Source）](../atlas/lighting/dramatic-single-source.md) — 单一强光源造成的极端明暗对比光型，是视觉系与戏剧肖像的照明基础。
- [黄金时刻逆光（Golden-Hour Backlight）](../atlas/lighting/golden-hour-backlight.md) — 日落前后低角度暖光，逆光勾勒发丝与身体轮廓，橙金色氛围。
- [霓虹实景光（Neon Practicals）](../atlas/lighting/neon-practicals.md) — 霓虹灯牌、串灯等画面内光源，提供彩色点/线状光与反射。
- [屏幕辉光（TV / CRT Glow）](../atlas/lighting/tv-crt-glow.md) — 电视机或 CRT 显示器打在脸上的冷色、闪烁的屏幕光，暗室中氛围独特。
- [暖色钨丝灯（Warm Tungsten）](../atlas/lighting/warm-tungsten.md) — 室内灯泡/台灯的暖黄低色温柔光，亲密、有生活感。
- [暗色唇（Dark Lips）](../atlas/makeup/dark-lips.md) — 黑、暗红、酒红、紫黑等深色唇妆，与白妆形成面部第二组强对比，是视觉系妆容的收尾重音。
- [水钻贴脸（Face Rhinestones）](../atlas/makeup/face-rhinestones.md) — 把水钻/珍珠/金属贴饰点缀在眼尾、眉心、颧骨或鼻梁，制造闪亮装饰。
- [霜状珠光眼影（Frosted Eyeshadow）](../atlas/makeup/frosted-eyeshadow.md) — 带珍珠/金属光泽的霜状眼影，大面积铺在眼皮甚至眉骨，是千禧年标志性眼妆。
- [镜面唇彩（Glossy Lips）](../atlas/makeup/glossy-lips.md) — 高光泽、丰盈的玻璃唇（常叠在裸色/粉色口红上），唇峰高光、微嘟。
- [长美甲片（Long Acrylic Nails）](../atlas/makeup/long-acrylic-nails.md) — 延长的亚克力美甲，常做法式、空气刷绘、水钻或火焰/爱心图案，是千禧辣妹标志。
- [深色烟熏眼（Dark Smoky Eye for Visual Kei）](../atlas/makeup/smoky-eye-visual-kei.md) — 以黑、灰、深紫、深红在眼周大面积晕染的眼妆，制造深邃眼窝与阴郁气质，视觉系的重型眼妆方案。
- [晒伤腮红（Sunburnt Blush）](../atlas/makeup/sunburnt-blush.md) — 横跨鼻梁、连接两颊的暖橘/粉色腮红，像日晒后的自然红晕，甜美而有元气。
- [泪袋妆 / 下眼睑强调（Tear Bag & Lower Lash Emphasis）](../atlas/makeup/tear-bag-makeup.md) — 刻意强调下眼睑与眼下区域的妆容——下眼线、眼下红晕、泪痕，制造病态、脆弱或阴郁的视觉系气质。
- [高挑细眉（Thin Arched Brows）](../atlas/makeup/thin-arched-brows.md) — 修剪得细而高挑的拱形眉，带成熟、精明或冷艳气质，是 90s 末–2000s 审美。
- [眼下亮片（Under-Eye Glitter）](../atlas/makeup/under-eye-glitter.md) — 在下眼睑/眼角点缀亮片或闪粉，像泪光一样闪烁，偶像舞台与甜辣写真常见。
- [白妆（White Foundation / 白塗り）](../atlas/makeup/white-foundation.md) — 刻意失真的极度白皙底妆，制造面具感与非人感，是视觉系妆容体系的共同基础。
- [上挑眼线（Sharp Winged Eyeliner）](../atlas/makeup/winged-eyeliner.md) — 向外上挑的锐利粗眼线，眼尾明显拉长，是视觉系眼妆的核心结构，制造锐利与攻击性。
- [牛仔与洗水（Denim Wash）](../atlas/material/denim-wash.md) — 不同洗水、做旧与装饰的牛仔布，Y2K 下装核心面料。
- [金葱面料（Gold Lamé）](../atlas/material/gold-lame.md) — 含金属细线、呈现金/银/古铜闪光的织物，暖调与舞台造型常用。
- [蕾丝与网纱（Lace and Tulle）](../atlas/material/lace-and-tulle.md) — 半透的蕾丝与网纱面料，制造繁复、脆弱、贵族式的华丽感，是 Angura 与哥特系视觉系的材质核心。
- [皮革与金属件（Leather and Hardware）](../atlas/material/leather-and-hardware.md) — 黑色皮革与银/铬金属五金件的组合，提供硬质、冷峻、有攻击性的质感对比，是视觉系的"骨架"材质。
- [液态铬（Liquid Chrome）](../atlas/material/liquid-chrome.md) — 像水银一样流动、镜面反射的金属表面，Cyber Metal 的核心材质。
- [PVC / 乙烯基（PVC / Vinyl）](../atlas/material/pvc-vinyl.md) — 光滑亮面、可透视的合成材料，反光强烈，未来感与性感并存。
- [缎面与天鹅绒（Satin and Velvet）](../atlas/material/satin-velvet.md) — 缎面的流动光泽与天鹅绒的深邃吸光，为视觉系提供"华美腐败"的高阶质感对比。
- [亮片 / 珠饰 / 水钻（Sequins & Beading）](../atlas/material/sequins-beading.md) — 满幅缝缀的亮片、珠串与切面水钻，产生密集闪烁高光。
- [薄纱 / 渔网（Sheer Mesh）](../atlas/material/sheer-mesh.md) — 透视网纱、渔网袜与网眼面料，叠穿与 Grunge 风格常用。
- [丝绒 / 天鹅绒（Velour / Velvet）](../atlas/material/velour.md) — 柔软、短绒、带柔和漫反射光泽的面料，运动套装与礼服皆用。
- [冷冽未来（Cold & Futuristic）](../atlas/mood/cold-futuristic.md) — 疏离、克制、无机质的科技冷感，Cyber Metal 的情绪。
- [怀旧微苦（Nostalgic & Bittersweet）](../atlas/mood/nostalgic-bittersweet.md) — 对逝去时光的温柔怀念，甜里带一点怅然，老 DV 与夕阳的情绪底色。
- [俏皮元气（Playful & Bubbly）](../atlas/mood/playful-bubbly.md) — 明亮、自信、停不下来的少女活力，甜辣偶像的情绪。
- [叛逆有攻击性（Rebellious & Angsty）](../atlas/mood/rebellious-angsty.md) — 慵懒、不屑、带一点愤怒的酷，Grunge Glam 的情绪。
- [海报墙（Band / Idol Posters）](../atlas/setting/band-posters.md) — 密集张贴的明星、乐队、动漫海报与杂志页，是年代审美的直接证据。
- [泳池 / 沙滩（Beach / Poolside）](../atlas/setting/beach-poolside.md) — 古铜阳光、湿润皮肤与水面反光的度假场景，适合身体高光与亮色泳装。
- [CD / MD 随身听（CD Player）](../atlas/setting/cd-player.md) — Discman、MD 随身听、光盘与有线耳机，千禧年移动音乐符号。
- [视觉系场景：空旷舞台与暗厅（Empty Stage & Dark Hall）](../atlas/setting/dark-stage.md) — 视觉系影像的典型环境——聚光灯下的空舞台、老旧洋馆、暗色室内，强调孤立与非日常。
- [台式电脑 + CRT（Desktop CRT Computer）](../atlas/setting/desktop-crt.md) — 米白色机箱、CRT 大屁股显示器、机械键盘、拨号上网的千禧桌面。
- [串灯 / 霓虹灯牌（Fairy Lights）](../atlas/setting/fairy-lights.md) — 缠绕的小灯泡串或小型霓虹灯牌，制造点状暖色光源。
- [翻盖手机（Flip Phone）](../atlas/setting/flip-phone.md) — 千禧年标志性的折叠/滑盖小手机，彩色外壳、天线、小外屏。
- [拍立得 / 傻瓜机（Instant Camera）](../atlas/setting/instant-camera.md) — 即时成像相机或胶片傻瓜机，闪光灯、彩色塑料机身。
- [熔岩灯（Lava Lamp）](../atlas/setting/lava-lamp.md) — 玻璃容器内缓慢变形的彩色蜡团，迷幻柔光。
- [商场 / 游戏厅（Mall / Arcade）](../atlas/setting/mall-arcade.md) — 千禧年购物中心、游戏厅或大头贴馆，霓虹、自动扶梯、游戏机与店铺招牌。
- [粉色浴室（Pink Bathroom）](../atlas/setting/pink-bathroom.md) — 粉/彩色瓷砖、陶瓷浴缸与镜面的复古浴室，闪光灯下有强烈千禧写真感。
- [毛绒玩具（Plushies / Beanie Babies）](../atlas/setting/plushies.md) — 床上与架子上的毛绒玩偶、Beanie Babies 豆豆娃，增添私密少女感。
- [千禧卧室（Poster-Covered Bedroom）](../atlas/setting/poster-bedroom.md) — 贴满海报、堆满私物的少女卧室，是 Y2K 人物向创作最私密、信息量最丰富的场景。
- [学校食堂 · 3D（School Cafeteria · 3D）](../atlas/setting/school-cafeteria-3d.md) — 2000s 学校食堂的低多边形 3D 场景——长条木桌、JK 学生群体用餐、午后阳光从大窗斜射入，温暖但孤独。
- [学校走廊监控视角（School Corridor CCTV）](../atlas/setting/school-corridor-cctv.md) — 2000s 学校走廊的低多边形 3D 场景——荧光灯、瓷砖墙、储物柜、尽头门，常配监控摄像头视角与 bounding box 叠层。
- [黄昏停车场/天台（Sunset Parking Lot）](../atlas/setting/sunset-parking-lot.md) — 露天停车场、天台或空旷街道在橙粉夕阳下的场景，逆光、长阴影、电影感。
- [电子宠物（Tamagotchi）](../atlas/setting/tamagotchi.md) — 蛋形掌上电子宠物机，挂绳、小液晶屏与按键。
- [瓷砖地下通道（Underground Passage · Tiled）](../atlas/setting/underground-passage-tiled.md) — 2000s 都市地下通道的低多边形 3D 场景——白色瓷砖墙、顶部荧光灯、贴满海报与告示，混凝土或瓷砖地面，昏暗中带暖光。
- [性别模糊表演者（Androgynous Performer）](../atlas/subject/character-archetypes/androgynous-performer.md) — 刻意模糊性别的角色原型——兼有男性与女性特征的美学主体，是日系视觉系与千禧时装影像的共同核心。
- [亚洲千禧偶像（Asian Millennium Idol）](../atlas/subject/character-archetypes/asian-millennium-idol.md) — 2000 年代前后东亚偶像工业制造的少女形象：精致、亲和、带舞台光泽，参考早安少女组、S.E.S.、滨崎步、安室奈美惠、宇多田光等，健康肤色或瓷白肌，笑容甜而有分寸。
- [低多边形 JK 角色（Low-Poly JK Character）](../atlas/subject/character-archetypes/lowpoly-jk-character.md) — 2000s 游戏风格的低多边形日本女高中生 3D 角色——块状三角面头发、贴图绘制五官、JK 制服（开衫+衬衫+蝴蝶结+格子裙），是 Retro Game CG 的核心人物原型。
- [混血空灵缪斯（Mixed Ethereal Muse）](../atlas/subject/character-archetypes/mixed-ethereal-muse.md) — 偏高端时尚杂志的混血少女形象：玻璃感眼神、空灵疏离、艺术化光影，常见于千禧年时装大片与先锋摄影师作品。
- [虚拟人偶（Virtual Doll / 3D）](../atlas/subject/character-archetypes/virtual-doll-3d.md) — 非真人的早期 3D 虚拟角色质感：光滑塑料/树脂皮肤、完美对称五官，参考千禧年游戏 CG、虚拟偶像与低多边形娃娃，带有 uncanny 的数字魅力。
- [欧美流行天后（Western Pop Diva）](../atlas/subject/character-archetypes/western-pop-diva.md) — 千禧年欧美 Teen Pop / R&B 天后形象：小麦色肌肤、健康自信的性感，参考 Britney Spears、Christina Aguilera、Jennifer Lopez、Destiny'
- [表情（Expressions）](../atlas/subject/expressions.md) — 镜头前表情与表演枚举。
- [面容与肤色（Face & Skin）](../atlas/subject/face-and-skin.md) — 人种特征、肤色与底妆质感枚举。
- [姿态（Poses）](../atlas/subject/poses.md) — 姿态与肢体语言枚举。
- [Baby Tee（短款露腰 T 恤）](../atlas/wardrobe/baby-tee.md) — 紧身、短至露腰的短袖 T 恤，常印标语、卡通或品牌徽标，是 Y2K 最具代表性的上装。
- [黑色修身西装（Black Tailored Suit）](../atlas/wardrobe/black-tailored-suit.md) — 视觉系最核心的服装单品——修身剪裁的全黑西装（含燕尾、长下摆变体），提供冷峻锐利的轮廓。
- [工装裤（Cargo Pants）](../atlas/wardrobe/cargo-pants.md) — 多口袋、宽松直筒的工装裤，受嘻哈与滑板文化影响，Grunge Glam 常用。
- [Chunky 复古球鞋（Chunky Sneakers）](../atlas/wardrobe/chunky-sneakers.md) — 厚底、线条繁复的复古运动鞋/老爹鞋，街头与运动套装搭配。
- [短款飞行员夹克（Cropped Bomber）](../atlas/wardrobe/cropped-bomber.md) — 截短版型的 MA-1 风格夹克，街头与甜辣混搭常用。
- [牛仔迷你裙（Denim Micro Skirt）](../atlas/wardrobe/denim-micro-skirt.md) — 极短的牛仔半身裙，常做旧、磨边或拼贴，甜辣造型高频单品。
- [挂脖上衣（Halter Top）](../atlas/wardrobe/halter-top.md) — 颈部系带、裸露肩膀与后背的上衣，千禧年正式与休闲场合皆流行。
- [高筒靴（Knee-High Boots）](../atlas/wardrobe/knee-high-boots.md) — 及膝靴，皮革/漆皮/翻折款，迷你裙与裤装皆可搭配，偏成熟强势。
- [低腰七分裤（Low-Rise Capris）](../atlas/wardrobe/low-rise-capris.md) — 小腿中部长度的卡普里裤，低腰、修身，2000 年代日常与街头常见。
- [低腰牛仔裤（Low-Rise Jeans）](../atlas/wardrobe/low-rise-jeans.md) — 腰线落在髋骨以下的牛仔裤，Y2K 最具标志性的下装，常配腰带与露腰上衣。
- [金属/亮片吊带（Metallic Cami）](../atlas/wardrobe/metallic-cami.md) — 细肩带、金属色或亮片材质的吊带背心，反光闪亮，是混搭层叠的核心内搭。
- [厚底凉鞋（Platform Sandals）](../atlas/wardrobe/platform-sandals.md) — 厚底/松糕底、绑带或搭扣的凉鞋，拉长比例，Y2K 甜辣与偶像造型标配。
- [薄开衫（Sheer / Knit Cardigan）](../atlas/wardrobe/sheer-cardigan.md) — 轻薄透视的针织或网纱开衫，松垮披搭，是混搭层叠造型的关键中层。
- [抹胸（Tube Top）](../atlas/wardrobe/tube-top.md) — 无肩带、贴合胸线的直筒抹胸，常以弹性针织或亮面材质制作。
- [丝绒运动套装（Velour Tracksuit）](../atlas/wardrobe/velour-tracksuit.md) — 连帽拉链外套 + 同料长裤的丝绒套装，Juicy Couture 带火的千禧名流制服。
- [PVC 亮面裤（Vinyl Pants）](../atlas/wardrobe/vinyl-pants.md) — 乙烯基/PVC 材质的亮面长裤，镜面反光，Cyber Metal 标志单品。

## guide（1）

- [📘 Obsidian 使用指南](../📘 Obsidian 使用指南.md) — 本 vault 的人类使用说明——打开方式、导航、图谱配色、编辑约定、模板与维护命令。

## index（1）

- [🏠 审美资产库 · 主页](../🏠 主页.md) — Obsidian 个人审美资产库的浏览入口——从这里进入风格、配方、元素与原料。

## moc（3）

- [🎬 配方 MOC](../🎬 配方.md) — 所有可用风格配方的浏览与状态看板——含产物评分与已知问题。
- [🗺️ 风格系谱 MOC](../🗺️ 风格系谱.md) — 所有风格运动与子风格的浏览地图——从家族根页进入各分支。
- [🧱 元素图鉴 MOC](../🧱 元素图鉴.md) — 14 个视觉维度的原子元素总入口——发型、妆容、材质、光影、质感等积木箱。
