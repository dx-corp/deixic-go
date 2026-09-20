# Changelog

## Unreleased

## [0.1.656](https://github.com/dx-corp/mono/compare/gen/go/v0.1.655...gen/go/v0.1.656) (2026-09-19)


### Features

* **memory:** atomically persist reviewed learning impact ([#9767](https://github.com/dx-corp/mono/issues/9767)) ([13d7893](https://github.com/dx-corp/mono/commit/13d7893f4c46f1451c67cbe34541bb0f1bc82365))

## [0.1.655](https://github.com/dx-corp/mono/compare/gen/go/v0.1.654...gen/go/v0.1.655) (2026-09-19)


### Features

* **code:** release private coding acceptance in 0.10.91 ([#9652](https://github.com/dx-corp/mono/issues/9652)) ([81e8153](https://github.com/dx-corp/mono/commit/81e8153ececc279b216058e7bdc943262d19a912))

## [0.1.654](https://github.com/dx-corp/mono/compare/gen/go/v0.1.653...gen/go/v0.1.654) (2026-09-18)


### Features

* **deixic:** make brand voice assets unlimited ([#9435](https://github.com/dx-corp/mono/issues/9435)) ([a35904b](https://github.com/dx-corp/mono/commit/a35904b67bc88db7628af9acf3bd42ed765b52a7))
* **deixic:** support multiple brand voices ([#9401](https://github.com/dx-corp/mono/issues/9401)) ([17daf3c](https://github.com/dx-corp/mono/commit/17daf3c27fa55806e8df65851f9dbb0cf362da27))
* **grid:** add durable admin and execution audit history ([#8996](https://github.com/dx-corp/mono/issues/8996)) ([937aee7](https://github.com/dx-corp/mono/commit/937aee749a14fe3da5661b31f12c09b4432b121e))
* **grid:** manage inference enrollment across Dex clients ([#8921](https://github.com/dx-corp/mono/issues/8921)) ([9913cce](https://github.com/dx-corp/mono/commit/9913cce5b8cfe14151fd4cf8edd5ad0fcd51ee8b))
* **maestro:** add opt-in experiments with cross-stack evidence ([#9180](https://github.com/dx-corp/mono/issues/9180)) ([b2e4144](https://github.com/dx-corp/mono/commit/b2e41445086b59840eabb097aa6e33036d9ba1b8))
* **platform:** require outcome contracts for declared coding work ([#9457](https://github.com/dx-corp/mono/issues/9457)) ([b4a0fc6](https://github.com/dx-corp/mono/commit/b4a0fc6c91f60497fa42068db2ae9f960763ebc5))
* **radar:** add Console-owned prospecting draft RPCs ([#9189](https://github.com/dx-corp/mono/issues/9189)) ([2f9d5d2](https://github.com/dx-corp/mono/commit/2f9d5d29a7db8a1aebad6638cea6771898e1b3bc))


### Bug Fixes

* **ci:** dispatch platform runtime without waiting on Maestro ([#9001](https://github.com/dx-corp/mono/issues/9001)) ([f36080f](https://github.com/dx-corp/mono/commit/f36080faedd90dd981dd125185fa326684361c1b))
* **dex:** put the turn identity on the tool-failure warns ([#8954](https://github.com/dx-corp/mono/issues/8954)) ([5b8fe33](https://github.com/dx-corp/mono/commit/5b8fe3384bffd46b836cfc4d3c1544d8d8414fb5))
* **dex:** surface governed tool approvals and resume the same call ([#9007](https://github.com/dx-corp/mono/issues/9007)) ([1d14b90](https://github.com/dx-corp/mono/commit/1d14b9015a767d158adf7a355b45ec29bff7f460))
* **gateway:** remap Gemini sanitized tool names onto declared Dex tools ([#9002](https://github.com/dx-corp/mono/issues/9002)) ([6a2013c](https://github.com/dx-corp/mono/commit/6a2013c6aee2f1989fbd2c15b1755e544305776f))
* **keys:** make provider revocation idempotent ([#9200](https://github.com/dx-corp/mono/issues/9200)) ([122eb53](https://github.com/dx-corp/mono/commit/122eb537087ce4aa381902e317a553d9c700c0ed))
* **meter:** make budget mutations idempotent ([#9199](https://github.com/dx-corp/mono/issues/9199)) ([02d26c5](https://github.com/dx-corp/mono/commit/02d26c51300be87558f07d8de473ec76f38d6ce0))
* **runtime:** derive runtime admission from capability catalog ([#8990](https://github.com/dx-corp/mono/issues/8990)) ([15b336c](https://github.com/dx-corp/mono/commit/15b336c392c5d36a7637f938baea69f9e165cdbb))
* **runtime:** recover audits and remove empty-claim polling ([#9003](https://github.com/dx-corp/mono/issues/9003)) ([1b7ecc8](https://github.com/dx-corp/mono/commit/1b7ecc81cb31bd2e39d3ca070ad1c5752681e37b))


### Performance Improvements

* reduce GCP NAT spend and expire temporary task homes ([#9421](https://github.com/dx-corp/mono/issues/9421)) ([63c27e4](https://github.com/dx-corp/mono/commit/63c27e4be5c9f039a30eaa575eb1a8b2cc75248d))


### Chores

* **deps:** bump the cargo group across 1 directory with 2 updates ([#9342](https://github.com/dx-corp/mono/issues/9342)) ([cf94c9a](https://github.com/dx-corp/mono/commit/cf94c9a949e588d68d2e1e54956f8f8e876d5aff))

## [0.1.653](https://github.com/evalops/platform/compare/gen/go/v0.1.652...gen/go/v0.1.653) (2026-08-15)


### Bug Fixes

* **computer:** make operating tool execution durable ([#6316](https://github.com/evalops/platform/issues/6316)) ([5dc22d3](https://github.com/evalops/platform/commit/5dc22d31394e9a1e6b336296473a58b2c7c7703e))

## [0.1.652](https://github.com/evalops/platform/compare/gen/go/v0.1.651...gen/go/v0.1.652) (2026-08-14)


### Features

* add Dex Apps spend explorer MVP ([#6042](https://github.com/evalops/platform/issues/6042)) ([f168a14](https://github.com/evalops/platform/commit/f168a146594285e0b45f9b17ef054bc77b9af178))
* **agentgateway:** add discovery-first control plane ([#6182](https://github.com/evalops/platform/issues/6182)) ([ef95f50](https://github.com/evalops/platform/commit/ef95f50b54c92f274e2e9f9692c9d55d463a6062))
* **artifacts:** bind artifacts to Operating Threads ([#6107](https://github.com/evalops/platform/issues/6107)) ([06452bd](https://github.com/evalops/platform/commit/06452bd7cef9bef0827635ef8f869c3cb95fada7))
* complete Dex Computer Rail runtime lifecycle ([#6044](https://github.com/evalops/platform/issues/6044)) ([46d9bd5](https://github.com/evalops/platform/commit/46d9bd56059b931f58d2a4ace74cf11aded76110))
* **computer:** certify verified episodes, effects, recovery, and proof ([#6056](https://github.com/evalops/platform/issues/6056)) ([8843a9f](https://github.com/evalops/platform/commit/8843a9f26731baeb79f88002667c4550eca84cd6))
* **dex:** implement the Agent Gateway product ([#6154](https://github.com/evalops/platform/issues/6154)) ([563d0fc](https://github.com/evalops/platform/commit/563d0fc3ce5f0d036f020d05989dc520320d0217))
* **evalcontrol:** add typed benchmark experiment contract ([#6172](https://github.com/evalops/platform/issues/6172)) ([32fc5c5](https://github.com/evalops/platform/commit/32fc5c570f23c2ca24fbdf1511cde645bfe67d47))
* **feature-flags:** add headless rust control service ([a7d9219](https://github.com/evalops/platform/commit/a7d921974e9bdcb9f0f13af53ad7b27c1bae21ef))
* **feature-flags:** add headless rust control service ([#6122](https://github.com/evalops/platform/issues/6122)) ([242cbe9](https://github.com/evalops/platform/commit/242cbe9d9494d31c3f4c265a95829921d4bcca0d))
* **observability:** propagate causal receipt identity ([aeee7d6](https://github.com/evalops/platform/commit/aeee7d6828609cba09b9d758c16fc4705026390f))
* **observability:** propagate causal receipt identity ([194df04](https://github.com/evalops/platform/commit/194df04cd4597ed22abb1e206eb40eb746598f4d))
* **platform:** expose typed app observability receipts ([#6261](https://github.com/evalops/platform/issues/6261)) ([7c5f50b](https://github.com/evalops/platform/commit/7c5f50bd9d56fde21fb4f9c902f21ed31093f8ac))


### Bug Fixes

* **feature-flags:** close control-plane review gaps ([6840c1f](https://github.com/evalops/platform/commit/6840c1fe86c80896b7204667eebc5e6e1dde3532))
* **feature-flags:** satisfy authz and sql ratchets ([1c0a600](https://github.com/evalops/platform/commit/1c0a600d95be86640f7a69aa655d5f7d35a3ba1d))
* harden customer outcome evidence integrity ([#6185](https://github.com/evalops/platform/issues/6185)) ([03cfd60](https://github.com/evalops/platform/commit/03cfd60249a87127219c35cc6f4ad8d371b23db8))
* **tool-executor:** persist typed failure codes ([#6167](https://github.com/evalops/platform/issues/6167)) ([dd9f276](https://github.com/evalops/platform/commit/dd9f2768bd82d781af0178c28a407a657c2fa744))


### Continuous Integration

* refresh exact-head validation ([7e23ce3](https://github.com/evalops/platform/commit/7e23ce3b17a1e6ccb080a7fc1606c994a1c2e053))
* retrigger protected checks ([4a76d70](https://github.com/evalops/platform/commit/4a76d70497e60a480b243e839ed378e1dedc95af))
* retry cancelled protected checks ([0d04855](https://github.com/evalops/platform/commit/0d04855df27c1c91aef2f65d187c3d051e11d62f))
* retry transient Rust toolchain setup ([87722fc](https://github.com/evalops/platform/commit/87722fc4ab395ac5adf12a165962cfb596163eab))


### Tests

* **dex:** pin typed app action authority ([#6252](https://github.com/evalops/platform/issues/6252)) ([077205a](https://github.com/evalops/platform/commit/077205a7ee0dfc85b1cb4e4b2c6dd39f90d4d98a))

## [0.1.651](https://github.com/evalops/platform/compare/gen/go/v0.1.650...gen/go/v0.1.651) (2026-08-10)


### Features

* **authz:** measure complete tenant boundaries ([#5820](https://github.com/evalops/platform/issues/5820)) ([5c8a705](https://github.com/evalops/platform/commit/5c8a7056a30e71c736a97c39d02d7d0856d8a863))
* **console:** InterruptOperatingThread stops pending Dex waits ([#5732](https://github.com/evalops/platform/issues/5732)) ([789802e](https://github.com/evalops/platform/commit/789802e585e87adb7a750ead69c6a7ff35d3c717))
* **console:** preserve typed terminal errors ([#5871](https://github.com/evalops/platform/issues/5871)) ([738c0c1](https://github.com/evalops/platform/commit/738c0c159d9b0a0bf2adf1431895182c06376dd6))
* **dex:** prewarm draft RunnerSessions ([#5800](https://github.com/evalops/platform/issues/5800)) ([c9dfb04](https://github.com/evalops/platform/commit/c9dfb04c4591b4eb2af42acd09c8a145485b1b0b))
* **llm-gateway:** add typed multi-provider failover ([#5779](https://github.com/evalops/platform/issues/5779)) ([21300c8](https://github.com/evalops/platform/commit/21300c8d635902f635f69cb1ddce61135963e408))
* **model-gateway:** persist provider exchange evidence ([#5854](https://github.com/evalops/platform/issues/5854)) ([6c1f079](https://github.com/evalops/platform/commit/6c1f079cfd88d7efd313560f6eeb32416b7b40f8))
* **operating:** add hosted front action lane ([#5894](https://github.com/evalops/platform/issues/5894)) ([1a13666](https://github.com/evalops/platform/commit/1a136666013e15afeb1c5461f547b35e8fbeb1ad))
* **platform-api:** mint scoped thread gateway browser tokens ([#5887](https://github.com/evalops/platform/issues/5887)) ([f1e8b78](https://github.com/evalops/platform/commit/f1e8b78b4d3bce23d0c1f714b2883ac029882ee0))
* **runner-host:** proxy initial actions ([#5892](https://github.com/evalops/platform/issues/5892)) ([443ab3f](https://github.com/evalops/platform/commit/443ab3fdf00349f70b0d20b22d26ff9ddbb86eaa))
* **ui:** ship workspace control and exact tenant switching ([#5828](https://github.com/evalops/platform/issues/5828)) ([9f903ed](https://github.com/evalops/platform/commit/9f903ed66c9653ec66a5b667b911c09424ebcee3))


### Bug Fixes

* **authz:** enforce staff RPC contract parity ([#5813](https://github.com/evalops/platform/issues/5813)) ([b491790](https://github.com/evalops/platform/commit/b4917901a4be69533e7e4235b3c9ddea686d0939))
* **operating:** persist typed hosted-front answers ([#5896](https://github.com/evalops/platform/issues/5896)) ([2bcdc82](https://github.com/evalops/platform/commit/2bcdc824e5ba08925da7885c0a2f23d72dd90f63))


### Chores

* refresh activation CAS verification ([df98730](https://github.com/evalops/platform/commit/df98730032ab73b92d121a198dc5ff04ebf85aed))


### Continuous Integration

* re-trigger PR checks after contract body fields ([82152c8](https://github.com/evalops/platform/commit/82152c8b9a74cca6569b2e3e7d241e50448f61c1))


### Platform

* **computer:** remove attach preflight round trip ([#5980](https://github.com/evalops/platform/issues/5980)) ([748135f](https://github.com/evalops/platform/commit/748135f2b81c7552dd51c2f1b41d8ec2890c3556))

## [0.1.650](https://github.com/evalops/platform/compare/gen/go/v0.1.649...gen/go/v0.1.650) (2026-08-03)


### Bug Fixes

* **ci:** restore main check baseline ([#5621](https://github.com/evalops/platform/issues/5621)) ([d6b85ba](https://github.com/evalops/platform/commit/d6b85ba92d0d64e23dd9a39e967d778325cfe8be))
* **lint:** collapse replaceable guards into let-chains ([#5628](https://github.com/evalops/platform/issues/5628)) ([e2a4891](https://github.com/evalops/platform/commit/e2a489101b05b9b2dd1363e9bcec8166a707622c))


### Documentation

* **llm-gateway:** point cache invalidation link at invalidate_credential ([#5630](https://github.com/evalops/platform/issues/5630)) ([fc97fbb](https://github.com/evalops/platform/commit/fc97fbb6f7a03118771467214feb1b0c0728e887))

## [0.1.649](https://github.com/evalops/platform/compare/gen/go/v0.1.648...gen/go/v0.1.649) (2026-08-02)


### Features

* complete Dex hosted Maestro cutover ([#5468](https://github.com/evalops/platform/issues/5468)) ([44767f5](https://github.com/evalops/platform/commit/44767f5bac482511f6f166ef869c8b7bcbd2fe39))
* **dex:** surface native chart artifacts end to end ([#5490](https://github.com/evalops/platform/issues/5490)) ([daedc98](https://github.com/evalops/platform/commit/daedc987926c35349574d076866a71930d8d732e))
* **skills:** add catalog provenance and queue readiness ([#5508](https://github.com/evalops/platform/issues/5508)) ([c396d55](https://github.com/evalops/platform/commit/c396d5593f19f9cf73a42504d75eb1d9a50ee293))

## [0.1.648](https://github.com/evalops/platform/compare/gen/go/v0.1.647...gen/go/v0.1.648) (2026-08-02)


### Features

* **costs:** add provider billing reconciliation ([#5473](https://github.com/evalops/platform/issues/5473)) ([c030768](https://github.com/evalops/platform/commit/c030768a1f358b9e969f7d698da518920abe057f))
* **runtime:** expose Maestro-safe channel capabilities ([#5456](https://github.com/evalops/platform/issues/5456)) ([b460107](https://github.com/evalops/platform/commit/b460107355e908b82fddd7f884769863f43abb89))
* **skills:** add curated skills library sources ([#5458](https://github.com/evalops/platform/issues/5458)) ([e0a93ee](https://github.com/evalops/platform/commit/e0a93ee51a3c5e47f59e5ad371a95508377ab957))


### Bug Fixes

* **console:** carry artifact intent through clarification turns ([#5476](https://github.com/evalops/platform/issues/5476)) ([51706d5](https://github.com/evalops/platform/commit/51706d542717fe9005a4dfff2796be5a8772ba74))
* **fleet:** make source-event intake exact ([#5455](https://github.com/evalops/platform/issues/5455)) ([e46a4ad](https://github.com/evalops/platform/commit/e46a4ad42828298b589de6c193dc7379dc26d751))
* **operating:** harden thread readiness and replay ([#5463](https://github.com/evalops/platform/issues/5463)) ([90554e8](https://github.com/evalops/platform/commit/90554e8f6fdc7836fe5a6c696d5f207961824ec8))

## [0.1.647](https://github.com/evalops/platform/compare/gen/go/v0.1.646...gen/go/v0.1.647) (2026-08-02)


### Bug Fixes

* **maestro:** project hosted execution identity ([#5441](https://github.com/evalops/platform/issues/5441)) ([70179f3](https://github.com/evalops/platform/commit/70179f3bb864e5a1e6874c84d1dbf55490a44536))
* **ui:** let Fleet use server-owned page size ([624ae91](https://github.com/evalops/platform/commit/624ae914aeeb8b34539ec1a855ae7ffc64910bd6))

## [0.1.646](https://github.com/evalops/platform/compare/gen/go/v0.1.645...gen/go/v0.1.646) (2026-08-01)


### Continuous Integration

* **previews:** keep teardown deployment listing a GET ([#5400](https://github.com/evalops/platform/issues/5400)) ([c767d08](https://github.com/evalops/platform/commit/c767d0836b88273759c33b1154d7d377a3973312))

## [0.1.645](https://github.com/evalops/platform/compare/gen/go/v0.1.644...gen/go/v0.1.645) (2026-07-31)


### Features

* **dex:** persist operating threads across runtime sessions ([#5388](https://github.com/evalops/platform/issues/5388)) ([d9cd314](https://github.com/evalops/platform/commit/d9cd314c995e03a633543d2f4a8dd7b4e534e3f6))
* **missions:** persist long-horizon autonomous execution ([#5375](https://github.com/evalops/platform/issues/5375)) ([f796078](https://github.com/evalops/platform/commit/f796078d0c0a99a50871f440a37130b08f402074))

## [0.1.644](https://github.com/evalops/platform/compare/gen/go/v0.1.643...gen/go/v0.1.644) (2026-07-31)


### Features

* preview Dex content policy drafts ([#5360](https://github.com/evalops/platform/issues/5360)) ([6d924ff](https://github.com/evalops/platform/commit/6d924ff7383c85464fb057a3d50237fdd9ec930a))


### Identity

* federate Maestro workload mTLS ([#5386](https://github.com/evalops/platform/issues/5386)) ([d60b4a6](https://github.com/evalops/platform/commit/d60b4a63c695258977bdb5d4b84c9891edeae7d5))

## [0.1.643](https://github.com/evalops/platform/compare/gen/go/v0.1.642...gen/go/v0.1.643) (2026-07-30)


### Features

* add Content and AI guardrails ([#5355](https://github.com/evalops/platform/issues/5355)) ([91278b6](https://github.com/evalops/platform/commit/91278b6a300416ddfd366a91b22f2f403b142629))
* **dex:** add artifact viewers and style guides ([#5348](https://github.com/evalops/platform/issues/5348)) ([ce75290](https://github.com/evalops/platform/commit/ce75290c35a5744b2d553e480e1d99697acff59a))
* **dex:** add document and presentation artifacts ([#5341](https://github.com/evalops/platform/issues/5341)) ([7b87f8e](https://github.com/evalops/platform/commit/7b87f8e36bbd654203cd28b69f00bc9da2a4a0ed))
* enforce style guide across Dex content ([#5353](https://github.com/evalops/platform/issues/5353)) ([ec537c3](https://github.com/evalops/platform/commit/ec537c32b0b629d78295d16c1c347ec5d9196ff5))

## [0.1.642](https://github.com/evalops/platform/compare/gen/go/v0.1.641...gen/go/v0.1.642) (2026-07-29)


### Features

* add product issue reporting and staff inbox ([7f67582](https://github.com/evalops/platform/commit/7f6758258791f66fb329456cbe744a705c0d9990))
* add product issue reporting and staff inbox ([8dbcf8e](https://github.com/evalops/platform/commit/8dbcf8e58ed12c6784f06e2d03197a9d2e2b85eb))

## [0.1.641](https://github.com/evalops/platform/compare/gen/go/v0.1.640...gen/go/v0.1.641) (2026-07-29)


### Features

* **dex:** add opt-in AI Spend Beat alerts ([6976276](https://github.com/evalops/platform/commit/69762767754745868396c016cdbf631e2c1dc7d2))
* **dex:** inspect durable agent quality ([bc55608](https://github.com/evalops/platform/commit/bc55608f2aeddc6dc34a93b3a88d355cff9ab2e1)) ([82e36cb](https://github.com/evalops/platform/commit/82e36cb5542303e440ff303eb8afb1d95ade0b8b)) ([e961dbe](https://github.com/evalops/platform/commit/e961dbe86ad190b210096a2a9ee4f747de6c9f54)) ([148a221](https://github.com/evalops/platform/commit/148a221ecff271358d548a8cfeef2cc043d1a0b6)) ([fcbfb0a](https://github.com/evalops/platform/commit/fcbfb0a35e8504bf27a4087f61fc7a6c25f3883f)) ([f16c3df](https://github.com/evalops/platform/commit/f16c3df4658a442c339eabb75fceb99c9d04c3d0)) ([8e5e61a](https://github.com/evalops/platform/commit/8e5e61a46342444cdf2792c11c9481a058b402af)) ([ff3ab34](https://github.com/evalops/platform/commit/ff3ab349ff1fcc3973821205deb69e5b058cea8e))
* **operating-chat:** persist correction feedback lifecycle ([3292a52](https://github.com/evalops/platform/commit/3292a520fca268f93308b687b157b86f304cee0d)) ([36dac92](https://github.com/evalops/platform/commit/36dac92d458d4ab5c4ec08cd60cca9ed8428b5a6)) ([34ab974](https://github.com/evalops/platform/commit/34ab974e01fc3e72f9f288b45b7e8117e41e4fbb)) ([84d4ad8](https://github.com/evalops/platform/commit/84d4ad80ebc6fd8bbb997b5cb6100a813f1b7b62)) ([6ada050](https://github.com/evalops/platform/commit/6ada05090beca6e446dea9cf02cf35703d303847)) ([587f748](https://github.com/evalops/platform/commit/587f7485e3ee68a14b0d0bacefa2fcdb1b923ad1)) ([467edf1](https://github.com/evalops/platform/commit/467edf123f223ff8c643e4dcbf2f7fddb5817b82)) ([49b0eec](https://github.com/evalops/platform/commit/49b0eec7af32ff8230473943bfd9438e5e8f6e8e)) ([d184c65](https://github.com/evalops/platform/commit/d184c653645e3ac98bffda9fb3aa2d5d77533726))


### Chores

* **gen:** regenerate console SDKs after merge (pinned buf 1.60.0) ([e245984](https://github.com/evalops/platform/commit/e2459848ce4713e5816fb3088ed902f5c467ac4a))

## [0.1.640](https://github.com/evalops/platform/compare/gen/go/v0.1.639...gen/go/v0.1.640) (2026-07-28)


### Features

* **channel-edge-slack:** adopt Slack Agent view context ([4dc9504](https://github.com/evalops/platform/commit/4dc9504991d8d893c67f18ea1a7401c5afbcb811))
* **channel-edge-slack:** preserve complete Slack Agent view package ancestry ([e4c93a9](https://github.com/evalops/platform/commit/e4c93a94f0539abde97c21a7d1dc38588e9fb71c)) ([45c8844](https://github.com/evalops/platform/commit/45c8844f6bd0797cb263316a39421c75fd3961fb)) ([a51fb24](https://github.com/evalops/platform/commit/a51fb244c41b9a1a36f881cceaba437fff381593)) ([2de40c8](https://github.com/evalops/platform/commit/2de40c88a4b56523d52f1ee28c4e610e65c128ce)) ([7245d32](https://github.com/evalops/platform/commit/7245d32975de67d057ec0a857263ddd988b1cb31)) ([04c1655](https://github.com/evalops/platform/commit/04c1655c3d39a78755ebc3f3a3cd7b2e64f374ba)) ([61df9aa](https://github.com/evalops/platform/commit/61df9aacdd935409abaf5bd95acf2bcef8aeb6f1))
* **console:** expand STAFF inference routing ([#5276](https://github.com/evalops/platform/issues/5276)) ([8212124](https://github.com/evalops/platform/commit/8212124f8a0b72075bd4e546d47710dc16104f40))

## [0.1.639](https://github.com/evalops/platform/compare/gen/go/v0.1.638...gen/go/v0.1.639) (2026-07-28)


### Features

* **console-staff:** add STAFF inference routing ([#5252](https://github.com/evalops/platform/issues/5252)) ([c39f331](https://github.com/evalops/platform/commit/c39f33106dfe8bcb6f6c5b2eec3262956155d8af))

## [0.1.638](https://github.com/evalops/platform/compare/gen/go/v0.1.637...gen/go/v0.1.638) (2026-07-28)


### Features

* enforce bounded connector action authority and budgets ([#5199](https://github.com/evalops/platform/issues/5199)) ([d252971](https://github.com/evalops/platform/commit/d252971af6048fbc3a74335222112b146699a4c2))

## [0.1.637](https://github.com/evalops/platform/compare/gen/go/v0.1.636...gen/go/v0.1.637) (2026-07-28)


### Features

* **tool-executor:** route allowlisted connector reads directly to connectors-rs ([#5169](https://github.com/evalops/platform/issues/5169)) ([882da36](https://github.com/evalops/platform/commit/882da36377e39ac3e9ea009d1b898f7f7df367b5))


### Bug Fixes

* **lint:** un-red three make lint targets on main ([#5226](https://github.com/evalops/platform/issues/5226)) ([702630c](https://github.com/evalops/platform/commit/702630c72dd1b66927d9d46bb36b38190aca9f51))
* **operating-chat:** fence answers to active turns ([#5131](https://github.com/evalops/platform/issues/5131)) ([78b3f54](https://github.com/evalops/platform/commit/78b3f548f8234f8e4182a9a8f5ab9a015f8b8845))


### Connectors

* close ConnectorRuntime/ConnectorActionDefinition tag collisions ([#5124](https://github.com/evalops/platform/issues/5124) stage 1) ([#5133](https://github.com/evalops/platform/issues/5133)) ([73193b9](https://github.com/evalops/platform/commit/73193b9b315c329e2ceaec205e1158c4b9a6a1e1))

## [0.1.636](https://github.com/evalops/platform/compare/gen/go/v0.1.635...gen/go/v0.1.636) (2026-07-27)


### Features

* add agentic Dex operating feedback ([#4806](https://github.com/evalops/platform/issues/4806)) ([5d4dd94](https://github.com/evalops/platform/commit/5d4dd941b1a0f2964b35a5a73df0f7dcf7a37d2a))
* add customer intelligence feedback ledger ([#4826](https://github.com/evalops/platform/issues/4826)) ([f6ce7da](https://github.com/evalops/platform/commit/f6ce7da1b8758422356a07e197f934820d874396))
* **apex:** add Dex end-to-end mission harness ([#4639](https://github.com/evalops/platform/issues/4639)) ([3db1880](https://github.com/evalops/platform/commit/3db1880aa0756499fe4cd88e1dff4e4ddc84843d))
* **billing:** add annual Stripe Checkout enrollment ([#5023](https://github.com/evalops/platform/issues/5023)) ([af53b99](https://github.com/evalops/platform/commit/af53b99755e171848a341b5f9110e805b2884830))
* **billing:** add tenant-scoped Stripe provider ([#5001](https://github.com/evalops/platform/issues/5001)) ([ae48b57](https://github.com/evalops/platform/commit/ae48b57ba660c69a1a09b26c3a6c58521f114e7b))
* **console-staff:** admin managed provider access control plane ([72c3115](https://github.com/evalops/platform/commit/72c31159588ba92edfa372e7a449e9018f032e98))
* **costs:** add typed provider snapshot ingestion ([#5024](https://github.com/evalops/platform/issues/5024)) ([6faf8c0](https://github.com/evalops/platform/commit/6faf8c02d02df8684df7d28da7f05ff3b5540a15))
* **costs:** render authoritative provider cost breakdowns ([#5035](https://github.com/evalops/platform/issues/5035)) ([68e3684](https://github.com/evalops/platform/commit/68e3684c59264a0553ffcc8f590c66f7a831f0e1))
* **dex:** action outcome contract and authorized connector dispatch ([#4623](https://github.com/evalops/platform/issues/4623)) ([3d00f3d](https://github.com/evalops/platform/commit/3d00f3d8a979e2de11869540e1182c2c9d7a83f2))
* **dex:** add proto-native temporal runtime context ([77e5b02](https://github.com/evalops/platform/commit/77e5b0206e7b382312f2c5453ad520265348037b))
* **dex:** capture natural, typed response feedback ([#5110](https://github.com/evalops/platform/issues/5110)) ([66e34ae](https://github.com/evalops/platform/commit/66e34ae03fe354b9d1367676a61fa4fd0a1a4f2c))
* **dex:** commitment-ledger nudge pass behind workspace opt-in ([#4882](https://github.com/evalops/platform/issues/4882)) ([1a2c13c](https://github.com/evalops/platform/commit/1a2c13c9e618f77f3f27cad54c042ceae61e1688))
* **dex:** durable proactive patterns and Cerebro attention wake ([#4621](https://github.com/evalops/platform/issues/4621)) ([3365b2d](https://github.com/evalops/platform/commit/3365b2d1512fee764d975f9ab4c2cd03dca5cf9e))
* **dex:** governed MCP client with receipted external tools ([#4458](https://github.com/evalops/platform/issues/4458)) ([a0d21cd](https://github.com/evalops/platform/commit/a0d21cd03e4db530afdaf7d1debcf270ac8452bb))
* **dex:** prove reversible production autonomy ([#4393](https://github.com/evalops/platform/issues/4393)) ([d699a27](https://github.com/evalops/platform/commit/d699a27b7972f2ca84615e3ffed4dd6cf14dbf7a))
* **dex:** publish typed product readiness ([#4680](https://github.com/evalops/platform/issues/4680)) ([797ad2d](https://github.com/evalops/platform/commit/797ad2d06b71ef34c897e757d879fd7f60ad414e))
* **dex:** receipted content guardrails on model output ([#4468](https://github.com/evalops/platform/issues/4468)) ([2e27621](https://github.com/evalops/platform/commit/2e27621bb23c068f084cca8df1d59f0f1d96558a))
* **governance:** add Rust Governance V2 control plane ([#4622](https://github.com/evalops/platform/issues/4622)) ([0aa7276](https://github.com/evalops/platform/commit/0aa72767e9745eff44e1fb52890ae67c9bd7fbe8))
* **identity:** capture first/last name and prompt when missing ([#4814](https://github.com/evalops/platform/issues/4814)) ([1e5fab1](https://github.com/evalops/platform/commit/1e5fab13dad6cdce4d2c4d815dec05f6b015b4dc))
* **identity:** issue scoped remote work credentials ([#4710](https://github.com/evalops/platform/issues/4710)) ([67c0ce3](https://github.com/evalops/platform/commit/67c0ce3dba3e9adeecca1c2821ea5a2c45d6bd0f))
* make Dex a multi-tenant Slack agent ([4505a11](https://github.com/evalops/platform/commit/4505a1126e3b743d91181f1cd12b219f2c866bd1))
* **platform-api:** replace dashboard service in Rust ([#5063](https://github.com/evalops/platform/issues/5063)) ([2651acd](https://github.com/evalops/platform/commit/2651acde695a9a9cb56ff91ee3e343675d903edb))
* **proto:** define Platform-owned Orb control contracts ([#4820](https://github.com/evalops/platform/issues/4820)) ([f4309d5](https://github.com/evalops/platform/commit/f4309d554ce7b216e3c5a1518d6554a66f6b3ace))
* **remoterunner:** add typed COMPUTER_SHELL/READ_FILE/WRITE_FILE step ops ([#5042](https://github.com/evalops/platform/issues/5042)) ([1ff9e6a](https://github.com/evalops/platform/commit/1ff9e6a6859dfdc800546d616c4dcfaad4fd39e2))
* **runtime:** apply fenced mission reports ([#5113](https://github.com/evalops/platform/issues/5113)) ([6f2cdc4](https://github.com/evalops/platform/commit/6f2cdc4df5255a5822077cf48d4708f3ed44b9ca))
* **runtime:** carry durable mission effect journals ([#5109](https://github.com/evalops/platform/issues/5109)) ([94bd2df](https://github.com/evalops/platform/commit/94bd2dfbebb62f2e25c8d0ae340735a3e0e9c6cb))
* **runtime:** define fenced mission execution boundary ([#5073](https://github.com/evalops/platform/issues/5073)) ([45aa224](https://github.com/evalops/platform/commit/45aa22442ed4db438a9409304b29b20f0dd86dac))
* **runtime:** run missions on a remote data plane ([#5116](https://github.com/evalops/platform/issues/5116)) ([1fb9a93](https://github.com/evalops/platform/commit/1fb9a936dd98b35b8977f8f8c505539dc8225a07))
* **runtime:** serve fenced mission claims ([#5111](https://github.com/evalops/platform/issues/5111)) ([4a6be0a](https://github.com/evalops/platform/commit/4a6be0a5f58295c6e445070d384821e6b882a561))
* **slack:** dispatch validated interactions into the shared operating conversation ([d2e184a](https://github.com/evalops/platform/commit/d2e184afdbb649ac42d193beace533810f525073))


### Bug Fixes

* close late platform review gaps ([#4798](https://github.com/evalops/platform/issues/4798)) ([d3a7a32](https://github.com/evalops/platform/commit/d3a7a32b1282e24356fd56ee49f59fde57bcf0ed))
* commit missing connectors TriggerSync generated code ([#4906](https://github.com/evalops/platform/issues/4906)) ([c012bf1](https://github.com/evalops/platform/commit/c012bf1a9420733a21edf46d3bdcf248c64f0276))
* **dex:** preserve attachments through queued turns ([#4619](https://github.com/evalops/platform/issues/4619)) ([e727a88](https://github.com/evalops/platform/commit/e727a886a9b5f18674d99d8078e99b97f52aef34))
* **proto:** align Dex policy update field with AIP-134 ([bbedca4](https://github.com/evalops/platform/commit/bbedca41ec0009b9d7f2d4eec94792d7fc74f7d0))
* **proto:** preserve Dex policy compatibility under AIP lint ([1bccf2d](https://github.com/evalops/platform/commit/1bccf2d12172dec20581d9d1b6b2c3dee5d6be5b))
* **proto:** preserve Dex policy compatibility under AIP-134 ([39bccc0](https://github.com/evalops/platform/commit/39bccc05c7f26be1d072a35f57748d09ed41b8db))
* **proto:** use native Dex policy suppression ([f11a36a](https://github.com/evalops/platform/commit/f11a36ae79c1d3d86945bb02ceef1dfb3ee62b04))
* silent-failure and cancel-unsafe heartbeat audit ([#4783](https://github.com/evalops/platform/issues/4783)) ([e23beb6](https://github.com/evalops/platform/commit/e23beb67ac0838e95cd1aa2c70bf27809c1ef901))

## [0.1.635](https://github.com/evalops/platform/compare/gen/go/v0.1.634...gen/go/v0.1.635) (2026-07-24)


### Features

* **console-staff:** admin managed provider access control plane ([72c3115](https://github.com/evalops/platform/commit/72c31159588ba92edfa372e7a449e9018f032e98))
* **platform-api:** replace dashboard service in Rust ([#5063](https://github.com/evalops/platform/issues/5063)) ([2651acd](https://github.com/evalops/platform/commit/2651acde695a9a9cb56ff91ee3e343675d903edb))
* **slack:** dispatch validated interactions into the shared operating conversation ([d2e184a](https://github.com/evalops/platform/commit/d2e184afdbb649ac42d193beace533810f525073))

## [0.1.634](https://github.com/evalops/platform/compare/gen/go/v0.1.633...gen/go/v0.1.634) (2026-07-24)


### Features

* **billing:** add annual Stripe Checkout enrollment ([#5023](https://github.com/evalops/platform/issues/5023)) ([af53b99](https://github.com/evalops/platform/commit/af53b99755e171848a341b5f9110e805b2884830))
* **billing:** add tenant-scoped Stripe provider ([#5001](https://github.com/evalops/platform/issues/5001)) ([ae48b57](https://github.com/evalops/platform/commit/ae48b57ba660c69a1a09b26c3a6c58521f114e7b))
* **console-staff:** admin managed provider access control plane ([72c3115](https://github.com/evalops/platform/commit/72c31159588ba92edfa372e7a449e9018f032e98))
* **costs:** add typed provider snapshot ingestion ([#5024](https://github.com/evalops/platform/issues/5024)) ([6faf8c0](https://github.com/evalops/platform/commit/6faf8c02d02df8684df7d28da7f05ff3b5540a15))
* **costs:** render authoritative provider cost breakdowns ([#5035](https://github.com/evalops/platform/issues/5035)) ([68e3684](https://github.com/evalops/platform/commit/68e3684c59264a0553ffcc8f590c66f7a831f0e1))
* **remoterunner:** add typed COMPUTER_SHELL/READ_FILE/WRITE_FILE step ops ([#5042](https://github.com/evalops/platform/issues/5042)) ([1ff9e6a](https://github.com/evalops/platform/commit/1ff9e6a6859dfdc800546d616c4dcfaad4fd39e2))
* **slack:** dispatch validated interactions into the shared operating conversation ([d2e184a](https://github.com/evalops/platform/commit/d2e184afdbb649ac42d193beace533810f525073))

## [0.1.633](https://github.com/evalops/platform/compare/gen/go/v0.1.632...gen/go/v0.1.633) (2026-07-19)


### Features

* **dex:** commitment-ledger nudge pass behind workspace opt-in ([#4882](https://github.com/evalops/platform/issues/4882)) ([1a2c13c](https://github.com/evalops/platform/commit/1a2c13c9e618f77f3f27cad54c042ceae61e1688))
* make Dex a multi-tenant Slack agent ([4505a11](https://github.com/evalops/platform/commit/4505a1126e3b743d91181f1cd12b219f2c866bd1))


### Bug Fixes

* commit missing connectors TriggerSync generated code ([#4906](https://github.com/evalops/platform/issues/4906)) ([c012bf1](https://github.com/evalops/platform/commit/c012bf1a9420733a21edf46d3bdcf248c64f0276))

## [0.1.632](https://github.com/evalops/platform/compare/gen/go/v0.1.631...gen/go/v0.1.632) (2026-07-19)


### Features

* add agentic Dex operating feedback ([#4806](https://github.com/evalops/platform/issues/4806)) ([5d4dd94](https://github.com/evalops/platform/commit/5d4dd941b1a0f2964b35a5a73df0f7dcf7a37d2a))
* add customer intelligence feedback ledger ([#4826](https://github.com/evalops/platform/issues/4826)) ([f6ce7da](https://github.com/evalops/platform/commit/f6ce7da1b8758422356a07e197f934820d874396))
* **dex:** add proto-native temporal runtime context ([77e5b02](https://github.com/evalops/platform/commit/77e5b0206e7b382312f2c5453ad520265348037b))
* **identity:** capture first/last name and prompt when missing ([#4814](https://github.com/evalops/platform/issues/4814)) ([1e5fab1](https://github.com/evalops/platform/commit/1e5fab13dad6cdce4d2c4d815dec05f6b015b4dc))
* **proto:** define Platform-owned Orb control contracts ([#4820](https://github.com/evalops/platform/issues/4820)) ([f4309d5](https://github.com/evalops/platform/commit/f4309d554ce7b216e3c5a1518d6554a66f6b3ace))


### Bug Fixes

* close late platform review gaps ([#4798](https://github.com/evalops/platform/issues/4798)) ([d3a7a32](https://github.com/evalops/platform/commit/d3a7a32b1282e24356fd56ee49f59fde57bcf0ed))

## [0.1.631](https://github.com/evalops/platform/compare/gen/go/v0.1.630...gen/go/v0.1.631) (2026-07-18)


### Features

* **dex:** action outcome contract and authorized connector dispatch ([#4623](https://github.com/evalops/platform/issues/4623)) ([3d00f3d](https://github.com/evalops/platform/commit/3d00f3d8a979e2de11869540e1182c2c9d7a83f2))
* **dex:** publish typed product readiness ([#4680](https://github.com/evalops/platform/issues/4680)) ([797ad2d](https://github.com/evalops/platform/commit/797ad2d06b71ef34c897e757d879fd7f60ad414e))

## [0.1.630](https://github.com/evalops/platform/compare/gen/go/v0.1.629...gen/go/v0.1.630) (2026-07-18)


### Features

* add native Slack channel edge foundation ([#4442](https://github.com/evalops/platform/issues/4442)) ([a0c0a0d](https://github.com/evalops/platform/commit/a0c0a0d1e27293170e30771bac08f870ffa320ba))
* **apex:** add Dex end-to-end mission harness ([#4639](https://github.com/evalops/platform/issues/4639)) ([3db1880](https://github.com/evalops/platform/commit/3db1880aa0756499fe4cd88e1dff4e4ddc84843d))
* **codex:** add bounded Agent Kit work contracts ([#4605](https://github.com/evalops/platform/issues/4605)) ([b0fee8c](https://github.com/evalops/platform/commit/b0fee8c063670d62f7197f04e313b093cb736bb6))
* **dex:** add Rust VFS file uploads ([#4609](https://github.com/evalops/platform/issues/4609)) ([c117758](https://github.com/evalops/platform/commit/c117758240489c84689ba89cd948286d7d4d0ffe))
* **dex:** cron-scheduled recurring missions with fenced claiming ([#4463](https://github.com/evalops/platform/issues/4463)) ([28ccbac](https://github.com/evalops/platform/commit/28ccbacfb0d8a9f013705bce82a2dc7176b4c2b1))
* **dex:** durable proactive patterns and Cerebro attention wake ([#4621](https://github.com/evalops/platform/issues/4621)) ([3365b2d](https://github.com/evalops/platform/commit/3365b2d1512fee764d975f9ab4c2cd03dca5cf9e))
* **dex:** governed MCP client with receipted external tools ([#4458](https://github.com/evalops/platform/issues/4458)) ([a0d21cd](https://github.com/evalops/platform/commit/a0d21cd03e4db530afdaf7d1debcf270ac8452bb))
* **dex:** prove reversible production autonomy ([#4393](https://github.com/evalops/platform/issues/4393)) ([d699a27](https://github.com/evalops/platform/commit/d699a27b7972f2ca84615e3ffed4dd6cf14dbf7a))
* **dex:** receipted content guardrails on model output ([#4468](https://github.com/evalops/platform/issues/4468)) ([2e27621](https://github.com/evalops/platform/commit/2e27621bb23c068f084cca8df1d59f0f1d96558a))
* **dex:** workspace skills as loadable procedures ([#4459](https://github.com/evalops/platform/issues/4459)) ([78c87db](https://github.com/evalops/platform/commit/78c87db2c498c29afcf63a6ebf9d341463a4f98a))
* **governance:** add Rust Governance V2 control plane ([#4622](https://github.com/evalops/platform/issues/4622)) ([0aa7276](https://github.com/evalops/platform/commit/0aa72767e9745eff44e1fb52890ae67c9bd7fbe8))
* **identity:** issue scoped remote work credentials ([#4710](https://github.com/evalops/platform/issues/4710)) ([67c0ce3](https://github.com/evalops/platform/commit/67c0ce3dba3e9adeecca1c2821ea5a2c45d6bd0f))


### Bug Fixes

* **dex:** preserve attachments through queued turns ([#4619](https://github.com/evalops/platform/issues/4619)) ([e727a88](https://github.com/evalops/platform/commit/e727a886a9b5f18674d99d8078e99b97f52aef34))
* **governance:** declare RPC authorization scopes ([#4608](https://github.com/evalops/platform/issues/4608)) ([0e24895](https://github.com/evalops/platform/commit/0e2489527d1b8eb07f30d93c302466800671f883))
* **proto:** align Dex policy update field with AIP-134 ([bbedca4](https://github.com/evalops/platform/commit/bbedca41ec0009b9d7f2d4eec94792d7fc74f7d0))
* **proto:** preserve Dex policy compatibility under AIP lint ([1bccf2d](https://github.com/evalops/platform/commit/1bccf2d12172dec20581d9d1b6b2c3dee5d6be5b))
* **proto:** preserve Dex policy compatibility under AIP-134 ([39bccc0](https://github.com/evalops/platform/commit/39bccc05c7f26be1d072a35f57748d09ed41b8db))
* **proto:** use native Dex policy suppression ([f11a36a](https://github.com/evalops/platform/commit/f11a36ae79c1d3d86945bb02ceef1dfb3ee62b04))
* silent-failure and cancel-unsafe heartbeat audit ([#4783](https://github.com/evalops/platform/issues/4783)) ([e23beb6](https://github.com/evalops/platform/commit/e23beb67ac0838e95cd1aa2c70bf27809c1ef901))

## [0.1.629](https://github.com/evalops/platform/compare/gen/go/v0.1.628...gen/go/v0.1.629) (2026-07-14)


### Features

* bind mission operations to runner sessions ([#4575](https://github.com/evalops/platform/issues/4575)) ([bb6917a](https://github.com/evalops/platform/commit/bb6917a850bfb3e8cd4ba573905e129b7415ba2a))

## [0.1.628](https://github.com/evalops/platform/compare/gen/go/v0.1.627...gen/go/v0.1.628) (2026-07-14)


### Features

* **dex:** search prior operating threads ([#4406](https://github.com/evalops/platform/issues/4406)) ([7bda7ac](https://github.com/evalops/platform/commit/7bda7ac0889d880dc3641b0d4b4aa6ab6f2a59a6))
* **platform:** workspace BYOK envelope encryption for managed credentials ([#4550](https://github.com/evalops/platform/issues/4550)) ([4cf100c](https://github.com/evalops/platform/commit/4cf100c42d9d75e7d088f3f01255c3bfbef4d551))


### Bug Fixes

* **proto:** land process v1 generated code ([#4555](https://github.com/evalops/platform/issues/4555)) ([955279c](https://github.com/evalops/platform/commit/955279c27469398fda3151431cde6018b58a6b96))

## [0.1.627](https://github.com/evalops/platform/compare/gen/go/v0.1.626...gen/go/v0.1.627) (2026-07-13)


### Features

* add Dex multichannel runtime and connector contracts ([#4428](https://github.com/evalops/platform/issues/4428)) ([8e78cb6](https://github.com/evalops/platform/commit/8e78cb6353046efbd0c84af2600c61ce93741d67))
* **dex:** bind routing decision to mission receipt ([#4504](https://github.com/evalops/platform/issues/4504)) ([7d11a43](https://github.com/evalops/platform/commit/7d11a43fa2205729dce70cb2253866e1e7913158))
* **dex:** build durable autonomous missions ([#4365](https://github.com/evalops/platform/issues/4365)) ([244d3f6](https://github.com/evalops/platform/commit/244d3f6704ad7ad0d4de7eeb2216816a50f9c243))
* **dex:** expose spend quality and causal attribution ([#4478](https://github.com/evalops/platform/issues/4478)) ([2d5c971](https://github.com/evalops/platform/commit/2d5c9717638df3be853bbf94951cebbf05be33d4))
* **dex:** persist staff wizard profile ([#4395](https://github.com/evalops/platform/issues/4395)) ([5392e06](https://github.com/evalops/platform/commit/5392e06258962b9a6f6b8b76dc23fefc815c580c))
* **dex:** resume missions from durable checkpoints ([#4420](https://github.com/evalops/platform/issues/4420)) ([c1552e0](https://github.com/evalops/platform/commit/c1552e06f1357d5f904f8e3edf8d16c1d0b30eae))
* **dex:** route tournaments by verified value ([#4486](https://github.com/evalops/platform/issues/4486)) ([11b14ea](https://github.com/evalops/platform/commit/11b14ea027518a2b0bcb0264aec8555cdef640ef))
* **fermata:** harden catalog lifecycle ([#4352](https://github.com/evalops/platform/issues/4352)) ([f8b63f7](https://github.com/evalops/platform/commit/f8b63f7382a0e9353a1d525292bfacd4f08d7c75))
* **identity:** add workspace-scoped service token contract ([#4439](https://github.com/evalops/platform/issues/4439)) ([ede3a9b](https://github.com/evalops/platform/commit/ede3a9badf383513635d461d54aeefb6054cc2b9))
* **platform:** expose callable capability features ([#4289](https://github.com/evalops/platform/issues/4289)) ([32921f9](https://github.com/evalops/platform/commit/32921f9a586b81d4c7396ee06f35d3c8d44b972f))
* **platform:** queue Dex operating turns through work ([#4291](https://github.com/evalops/platform/issues/4291)) ([e2d273b](https://github.com/evalops/platform/commit/e2d273be02722aa1a2018117f5713a952e6dd464))
* **remote-runner:** integrate sandboxwich hosted runtimes ([#4358](https://github.com/evalops/platform/issues/4358)) ([8f2c0eb](https://github.com/evalops/platform/commit/8f2c0eb4932fbfdc5a3f811448be2613b49756ca))
* **runner-host:** execute sandbox steps and checkpoints ([#4389](https://github.com/evalops/platform/issues/4389)) ([6cc7283](https://github.com/evalops/platform/commit/6cc7283cdc14fdbe9d203c73e38e1b9982edaa3b))
* **settings:** build operational staff administration ([#4408](https://github.com/evalops/platform/issues/4408)) ([b688028](https://github.com/evalops/platform/commit/b688028b25835e159932bdc17c05f43304a7133b))
* **tournament:** add durable run foundation ([#4379](https://github.com/evalops/platform/issues/4379)) ([5d2e982](https://github.com/evalops/platform/commit/5d2e9828278f70bbeaed8f1b501021d05050cb1a))
* **tournament:** execute typed candidates in platform worker ([#4390](https://github.com/evalops/platform/issues/4390)) ([362c66a](https://github.com/evalops/platform/commit/362c66ae7e29a38eacd413d966c0d53d97877556))
* **tournament:** persist selection provenance ([#4493](https://github.com/evalops/platform/issues/4493)) ([8d9f491](https://github.com/evalops/platform/commit/8d9f4915a99888c048d8fe033cd1cd31d5bbf5e6))
* **tournament:** terminalize no-route decisions ([#4492](https://github.com/evalops/platform/issues/4492)) ([977519a](https://github.com/evalops/platform/commit/977519a8d13bbaac74d67456a5bbe099e90c1111))


### Bug Fixes

* **dex:** carry typed costs context in spend canary ([e181440](https://github.com/evalops/platform/commit/e18144027a2e49e7d995827849910e3693012503))
* **dex:** carry typed costs context in spend canary ([587557e](https://github.com/evalops/platform/commit/587557e465ea107ce2123e5b6dfa513d299c9d25))
* **dex:** use generated Connect canary client ([#4490](https://github.com/evalops/platform/issues/4490)) ([b7e2f5b](https://github.com/evalops/platform/commit/b7e2f5b0319467df962965e0000ee5851e3894e5))

## [0.1.626](https://github.com/evalops/platform/compare/gen/go/v0.1.625...gen/go/v0.1.626) (2026-07-07)


### Bug Fixes

* keys: add managed customer credential upload flow ([#4238](https://github.com/evalops/platform/issues/4238)) ([8876a47](https://github.com/evalops/platform/commit/8876a47b265ea9e79db2f44a72fd65416c4ff2e8))
* surface connector setup requirements ([74afbd0](https://github.com/evalops/platform/commit/74afbd0132a5bb6a70f774a4879c6f6140f75388))

### Documentation

* refresh internal tooling guard report ([#4272](https://github.com/evalops/platform/issues/4272)) ([1ad6db4](https://github.com/evalops/platform/commit/1ad6db46760f2ff394acaef01fba2796a61c3f2a))

### Miscellaneous

* merge main into release branch ([9497f81](https://github.com/evalops/platform/commit/9497f8168a37dbfd7dc482d664e50c228178bb7b))

## [0.1.625](https://github.com/evalops/platform/compare/gen/go/v0.1.624...gen/go/v0.1.625) (2026-07-05)


### Bug Fixes

* harden Cursor cost sync follow-ups ([#4206](https://github.com/evalops/platform/issues/4206)) ([b2692fe](https://github.com/evalops/platform/commit/b2692fe7347c6835db3be983d5f0ee6552140228))

## [0.1.624](https://github.com/evalops/platform/compare/gen/go/v0.1.623...gen/go/v0.1.624) (2026-07-04)


### Features

* build runtime service slices ([#4139](https://github.com/evalops/platform/issues/4139)) ([5640e6c](https://github.com/evalops/platform/commit/5640e6c2b37d762815743362080634ecaca4f68f))
* **llm-gateway:** add adaptive routing ([#4141](https://github.com/evalops/platform/issues/4141)) ([ec9d697](https://github.com/evalops/platform/commit/ec9d697cb12d4bdb14e9d69243dcc914880b71f9))


### Miscellaneous Chores

* merge main into release branch ([8b7ef63](https://github.com/evalops/platform/commit/8b7ef63418d663154dcbbf00ec6121a6281aaa9e))

## [0.1.623](https://github.com/evalops/platform/compare/gen/go/v0.1.622...gen/go/v0.1.623) (2026-07-04)


### Features

* add MCP gateway policy core ([#4057](https://github.com/evalops/platform/issues/4057)) ([09ece15](https://github.com/evalops/platform/commit/09ece15dca626d89b5c51ee643fe1151d56ae7a7))
* add sessions ingest rpc ([#4012](https://github.com/evalops/platform/issues/4012)) ([037da48](https://github.com/evalops/platform/commit/037da4823fe5e12b7cd84b8771457e4e59ebcd0e))
* add typed operating chat turn routing ([#4026](https://github.com/evalops/platform/issues/4026)) ([a957808](https://github.com/evalops/platform/commit/a95780847f4aff88fa3975c3bd4d08ddc367bed3))
* **dex:** add backend llm tool runner ([#4022](https://github.com/evalops/platform/issues/4022)) ([8cec208](https://github.com/evalops/platform/commit/8cec208e6b5bf511e58578d8f1b442dd3722fbb6))
* **integrations:** surface connector lifecycle state ([#4035](https://github.com/evalops/platform/issues/4035)) ([b9b71b7](https://github.com/evalops/platform/commit/b9b71b78585b7512776b97a1596c6f85f489f731))
* **llm-gateway:** harden routing contract ([7416366](https://github.com/evalops/platform/commit/741636643ddcddf094e325fd63d483949f0bb062))


### Bug Fixes

* **llm-gateway:** add rust gateway boundary ([6f366a9](https://github.com/evalops/platform/commit/6f366a997b42fbe3d0c154fa8e411b67ff189da0))
* **llm-gateway:** declare rpc authz metadata ([101b116](https://github.com/evalops/platform/commit/101b11678e93b8269c0adc84a2db8f3afca554bd))
* preserve evalcontrol acknowledgment notes ([#4014](https://github.com/evalops/platform/issues/4014)) ([a5908ab](https://github.com/evalops/platform/commit/a5908abf297eb3a24b9d84dc1402fc2a365f8017))

## [0.1.622](https://github.com/evalops/platform/compare/gen/go/v0.1.621...gen/go/v0.1.622) (2026-07-02)


### Features

* add console boot read model ([#3880](https://github.com/evalops/platform/issues/3880)) ([453f8e1](https://github.com/evalops/platform/commit/453f8e1f9c9449688fab8fa021f8dd1067f83206))
* **connectors:** expose provider runtime metadata ([e49d858](https://github.com/evalops/platform/commit/e49d858c5564aa69c901644633478b7bd75a1ca1))
* pass connector runtime metadata through console tiles ([5371b62](https://github.com/evalops/platform/commit/5371b62d5fde03a141eb062fb5a38f2f97db776d))
* **platform:** add Rust migration hardening gates ([#3979](https://github.com/evalops/platform/issues/3979)) ([f7d434a](https://github.com/evalops/platform/commit/f7d434a47c38c3e171e4dbda0e3d87a493aa1ef3))
* **platform:** add Rust platform primitive architecture ([78a81ec](https://github.com/evalops/platform/commit/78a81ecf461c32d66c23686e6d811c8f26779a16))


### Bug Fixes

* **build:** retire stale Bazel surface ([e35601e](https://github.com/evalops/platform/commit/e35601e6da8b1591a3e4b6a5737b0679d95697f5))

## [0.1.621](https://github.com/evalops/platform/compare/gen/go/v0.1.620...gen/go/v0.1.621) (2026-06-30)


### Bug Fixes

* wire remote-run receipt action ([#3808](https://github.com/evalops/platform/issues/3808)) ([72a81c8](https://github.com/evalops/platform/commit/72a81c896618d420b5ccd5c161f6da49cf590891))

## [0.1.620](https://github.com/evalops/platform/compare/gen/go/v0.1.619...gen/go/v0.1.620) (2026-06-30)


### Bug Fixes

* query operating turns without coordinator fanout ([#3836](https://github.com/evalops/platform/issues/3836)) ([c249201](https://github.com/evalops/platform/commit/c24920131c0d561194425d8d0dd543d0bfba774c))

## [0.1.619](https://github.com/evalops/platform/compare/gen/go/v0.1.618...gen/go/v0.1.619) (2026-06-29)


### Features

* **console:** make staff context native to Dex chat ([11f5496](https://github.com/evalops/platform/commit/11f549678005c1008344248f5b00354db11046c6))
* **console:** make staff context native to Dex chat ([4512990](https://github.com/evalops/platform/commit/45129905e65344f579942a3931461802c256eb53))

## [0.1.618](https://github.com/evalops/platform/compare/gen/go/v0.1.617...gen/go/v0.1.618) (2026-06-28)


### Features

* **settings:** add workspace RBAC summaries ([#3784](https://github.com/evalops/platform/issues/3784)) ([6f5d885](https://github.com/evalops/platform/commit/6f5d885072b901c72f9ede6ac2d107a8442c3f3b))

## [0.1.617](https://github.com/evalops/platform/compare/gen/go/v0.1.616...gen/go/v0.1.617) (2026-06-26)


### Bug Fixes

* **console:** check model refs without resolving secrets ([f200346](https://github.com/evalops/platform/commit/f200346f7d6db3e94a495a7337011033c69f3a4b))
* **console:** read model access from provider refs ([107e5f0](https://github.com/evalops/platform/commit/107e5f099afd2cabe955e1b113f9f735d0b0d019))

## [0.1.616](https://github.com/evalops/platform/compare/gen/go/v0.1.615...gen/go/v0.1.616) (2026-06-25)


### Bug Fixes

* make settings break glass durable ([#3619](https://github.com/evalops/platform/issues/3619)) ([1cf78e4](https://github.com/evalops/platform/commit/1cf78e48b48a103046fdb726b3f41a98f4a87258))

## [0.1.615](https://github.com/evalops/platform/compare/gen/go/v0.1.614...gen/go/v0.1.615) (2026-06-21)


### Features

* **identity:** add proto messages and services for workspace, team, and invitation ([#3476](https://github.com/evalops/platform/issues/3476)) ([02fae15](https://github.com/evalops/platform/commit/02fae15900c0feca8061640402220508e6fd7530))


### Bug Fixes

* **identity:** security hardening for workspace, team, and invitation handlers ([#3483](https://github.com/evalops/platform/issues/3483)) ([9435c2e](https://github.com/evalops/platform/commit/9435c2e956652a7255d5ec043b946b5c1d7bd4b7))

## [0.1.614](https://github.com/evalops/platform/compare/gen/go/v0.1.613...gen/go/v0.1.614) (2026-06-21)


### Features

* **audit:** add auditctl export + /settings/audit page ([#3296](https://github.com/evalops/platform/issues/3296)) ([#3454](https://github.com/evalops/platform/issues/3454)) ([ab41001](https://github.com/evalops/platform/commit/ab410010638f54a23b523c5d275c1864408f4dd8))

## [0.1.613](https://github.com/evalops/platform/compare/gen/go/v0.1.612...gen/go/v0.1.613) (2026-06-20)


### Features

* **meter:** add IngestWideEventBatch RPC for FE telemetry batch flushes ([#3439](https://github.com/evalops/platform/issues/3439)) ([0b1648b](https://github.com/evalops/platform/commit/0b1648b6e56ee34a6887bf37beeb5039b902c7a0))

## [0.1.612](https://github.com/evalops/platform/compare/gen/go/v0.1.611...gen/go/v0.1.612) (2026-06-20)


### Features

* **console:** workspace source pinning (BE) ([#3427](https://github.com/evalops/platform/issues/3427)) ([6f4aee8](https://github.com/evalops/platform/commit/6f4aee8965c51ccc19a934bd78c10893da3b2a32))

## [0.1.611](https://github.com/evalops/platform/compare/gen/go/v0.1.610...gen/go/v0.1.611) (2026-06-16)


### Features

* **lint:** self-validating RPC risk-level check ([#3301](https://github.com/evalops/platform/issues/3301)) ([137e9a3](https://github.com/evalops/platform/commit/137e9a3feb338dee9e88d51b1223518c9b6b63a9))

## [0.1.610](https://github.com/evalops/platform/compare/gen/go/v0.1.609...gen/go/v0.1.610) (2026-06-16)


### Bug Fixes

* **bazel:** add transitive BUILD targets for dashboards graph ([#3293](https://github.com/evalops/platform/issues/3293)) ([822abdd](https://github.com/evalops/platform/commit/822abdd0f883d62d1904db2c68909e786b3a3dc1))

## [0.1.609](https://github.com/evalops/platform/compare/gen/go/v0.1.608...gen/go/v0.1.609) (2026-06-16)


### Features

* **oauth:** OAuth UX followups — 8 of 12 shipped ([#3273](https://github.com/evalops/platform/issues/3273)) ([0d1273e](https://github.com/evalops/platform/commit/0d1273e261d981da59227d0c9e9c38fd80e4ad92))

## [0.1.608](https://github.com/evalops/platform/compare/gen/go/v0.1.607...gen/go/v0.1.608) (2026-06-16)


### Features

* **connectors:** scaffold OAuth flow RPCs ([#3262](https://github.com/evalops/platform/issues/3262)) ([2c3452d](https://github.com/evalops/platform/commit/2c3452db290b87ba9a24a62d073a1ec5db51db91))
* **dashboards:** scaffold DashboardService for agent-buildable apps ([#3269](https://github.com/evalops/platform/issues/3269)) ([f2c4cd8](https://github.com/evalops/platform/commit/f2c4cd8991d2b660d8d8933922f3749c899b8cbc))

## [0.1.607](https://github.com/evalops/platform/compare/gen/go/v0.1.606...gen/go/v0.1.607) (2026-06-14)


### Features

* add context library ingestion surface ([#3230](https://github.com/evalops/platform/issues/3230)) ([1a952cc](https://github.com/evalops/platform/commit/1a952cc3e4a03003d092d0f68bc249821c0f8570))

## [0.1.606](https://github.com/evalops/platform/compare/gen/go/v0.1.605...gen/go/v0.1.606) (2026-06-13)


### Features

* add billing subscription API ([b999510](https://github.com/evalops/platform/commit/b9995104ce428360da8c355c05bac3e5ba0b8670)), closes [#2997](https://github.com/evalops/platform/issues/2997)

## [0.1.605](https://github.com/evalops/platform/compare/gen/go/v0.1.604...gen/go/v0.1.605) (2026-06-13)


### Bug Fixes

* **agentruntime:** paginate run event listing ([#3115](https://github.com/evalops/platform/issues/3115)) ([#3180](https://github.com/evalops/platform/issues/3180)) ([18f5b5b](https://github.com/evalops/platform/commit/18f5b5bd8a817bce604fa6178ebd6d68b4072f89))
* annotate notification workspace scopes ([#3135](https://github.com/evalops/platform/issues/3135)) ([043549c](https://github.com/evalops/platform/commit/043549ca939f784d42d241051d31e4e2d843a54e))
* **authmw:** enforce repeated scope fields ([#3136](https://github.com/evalops/platform/issues/3136)) ([645f7bc](https://github.com/evalops/platform/commit/645f7bc1ac451e39cfc35bc37f0ac8bc28f1fecc))
* detect nested tenant scope guard paths ([#3111](https://github.com/evalops/platform/issues/3111)) ([#3164](https://github.com/evalops/platform/issues/3164)) ([8b03c15](https://github.com/evalops/platform/commit/8b03c15bb8e318aa54e2317f8631bccd770d641d))
* **entities:** delete retired relationships slice ([#3092](https://github.com/evalops/platform/issues/3092)) ([#3165](https://github.com/evalops/platform/issues/3165)) ([8a408b1](https://github.com/evalops/platform/commit/8a408b13c392cbf53e4d7014e84330fbd85cb122))

## [0.1.604](https://github.com/evalops/platform/compare/gen/go/v0.1.603...gen/go/v0.1.604) (2026-06-08)


### Features

* add enterprise workspace settings ([be2136d](https://github.com/evalops/platform/commit/be2136df625ad2add554415514352b920dca9ab5))
* add enterprise workspace settings ([d8649ac](https://github.com/evalops/platform/commit/d8649ac52567e1f6f3fd566d464e536fc90397c6))
* add enum-backed workspace settings contracts ([d9e077d](https://github.com/evalops/platform/commit/d9e077d043d58635a231b6effc1b386b32a7ec05))
* add workspace settings audit history ([2ac7a07](https://github.com/evalops/platform/commit/2ac7a07e15c1cc49b8ed75e4d85b7bc87d575c49))
* build enterprise settings ownership ([443f3de](https://github.com/evalops/platform/commit/443f3de95eebd2ce32be09ff39df4228304425d9))
* enforce workspace settings rbac ([82f6d69](https://github.com/evalops/platform/commit/82f6d690144487af0be7239fcb1dd07329ca9f9e))
* enforce workspace settings RBAC ([20b0717](https://github.com/evalops/platform/commit/20b07175820e0b54af27b32f2f0b4a645f48f574))
* fully enable workspace settings ([d6c5022](https://github.com/evalops/platform/commit/d6c50224d9845b4d5dd516a1706b1b852aef1d0f))
* fully enable workspace settings ([60433b3](https://github.com/evalops/platform/commit/60433b30c91b3882395c6a4a0224375be2673741))


### Bug Fixes

* require verified email for domain policies ([2211934](https://github.com/evalops/platform/commit/221193478d1d2122704b0872eb93fe9169c37087))

## [0.1.603](https://github.com/evalops/platform/compare/gen/go/v0.1.602...gen/go/v0.1.603) (2026-06-06)


### Bug Fixes

* back settings with real workspace state ([#3034](https://github.com/evalops/platform/issues/3034)) ([293f57d](https://github.com/evalops/platform/commit/293f57d6fad69086639f89b4f7e03528bae72af1))

## [0.1.602](https://github.com/evalops/platform/compare/gen/go/v0.1.601...gen/go/v0.1.602) (2026-06-05)


### Features

* **ui:** wire Tier 2 backend endpoints into UI ([#3013](https://github.com/evalops/platform/issues/3013)) ([962bb9d](https://github.com/evalops/platform/commit/962bb9dece72ed7293409e3a0154ae8417391207))


### Bug Fixes

* **console:** require scoped read authz on workspace data RPCs (security) ([#3015](https://github.com/evalops/platform/issues/3015)) ([a98afaf](https://github.com/evalops/platform/commit/a98afaf3b8995c7ca8396c46f9db069a31d74f08))

## [0.1.601](https://github.com/evalops/platform/compare/gen/go/v0.1.600...gen/go/v0.1.601) (2026-06-05)


### Features

* **ui:** wire workspace org from OAuth, connect authority posture API, remove dead fixtures ([#2984](https://github.com/evalops/platform/issues/2984)) ([934fc88](https://github.com/evalops/platform/commit/934fc88b307279a884d0c8a170334cefdf2d61bb))

## [0.1.600](https://github.com/evalops/platform/compare/gen/go/v0.1.599...gen/go/v0.1.600) (2026-06-05)


### Features

* add agent workforce evidence submission ([#2971](https://github.com/evalops/platform/issues/2971)) ([31be0f8](https://github.com/evalops/platform/commit/31be0f86eb2acd73767101393580e71e829a3116))

## [0.1.599](https://github.com/evalops/platform/compare/gen/go/v0.1.598...gen/go/v0.1.599) (2026-06-05)


### Features

* expose configured-only agent workforce source readiness ([#2954](https://github.com/evalops/platform/issues/2954)) ([b236ab0](https://github.com/evalops/platform/commit/b236ab0ceb09976fb78682d19c782ead58137592))

## [0.1.598](https://github.com/evalops/platform/compare/gen/go/v0.1.597...gen/go/v0.1.598) (2026-06-04)


### Features

* add multi-source workforce onboarding evidence ([2a322ac](https://github.com/evalops/platform/commit/2a322ac391e92706d5af9c534075e10cdec8cad3))

## [0.1.597](https://github.com/evalops/platform/compare/gen/go/v0.1.596...gen/go/v0.1.597) (2026-06-04)


### Features

* add workforce approval queue rollups ([#2928](https://github.com/evalops/platform/issues/2928)) ([e8ae48e](https://github.com/evalops/platform/commit/e8ae48e1df51a03e06a5a738fd9b5a1409b0f46d))

## [0.1.596](https://github.com/evalops/platform/compare/gen/go/v0.1.595...gen/go/v0.1.596) (2026-06-03)


### Features

* add agent workforce proof summary ([#2894](https://github.com/evalops/platform/issues/2894)) ([ec778da](https://github.com/evalops/platform/commit/ec778daab06b33e8217cfaaedf0711fc61222a0f))

## [0.1.595](https://github.com/evalops/platform/compare/gen/go/v0.1.594...gen/go/v0.1.595) (2026-06-03)


### Features

* carry action authority proof states for Agent Workforce ([#2887](https://github.com/evalops/platform/issues/2887)) ([ea3989c](https://github.com/evalops/platform/commit/ea3989c95e4345ffcc6d653a716cfa238ec6d353))

## [0.1.594](https://github.com/evalops/platform/compare/gen/go/v0.1.593...gen/go/v0.1.594) (2026-06-03)


### Features

* add Agent Workforce approval disablement reason ([#2882](https://github.com/evalops/platform/issues/2882)) ([2071c1d](https://github.com/evalops/platform/commit/2071c1dd4232eb99998da8bc5f9c2c720e4df3f2))
* add Agent Workforce endpoint guardrail posture ([#2886](https://github.com/evalops/platform/issues/2886)) ([6b3360b](https://github.com/evalops/platform/commit/6b3360b756984ec5048b3e80f017f345fd4e5cb5))
* add agent workforce read records ([#2879](https://github.com/evalops/platform/issues/2879)) ([e3c570d](https://github.com/evalops/platform/commit/e3c570d8c9673e2b3a56b0529ef497c140685bc4))
* add canonical trace review contract ([#2783](https://github.com/evalops/platform/issues/2783)) ([f0bff57](https://github.com/evalops/platform/commit/f0bff5707b62d43b45d211d41e72fbc36b12484b))
* add console authority posture ledger ([#2871](https://github.com/evalops/platform/issues/2871)) ([158d1ee](https://github.com/evalops/platform/commit/158d1eeae6470c4eee961203d4149c54028a2cb2))
* add console security decision packet ([#2866](https://github.com/evalops/platform/issues/2866)) ([ad1629d](https://github.com/evalops/platform/commit/ad1629dd6f6132837c700721669dfd194766a1f1))
* add Core status API and Slack parity ([#2584](https://github.com/evalops/platform/issues/2584)) ([e9425d7](https://github.com/evalops/platform/commit/e9425d758614024b0ba1fe7ee084a408ef040e41))
* add native agent event receipts ([#2863](https://github.com/evalops/platform/issues/2863)) ([dee014b](https://github.com/evalops/platform/commit/dee014b69e5216d307891ca073fe7e9fc609e423))
* add records service contract ([9a5b9cb](https://github.com/evalops/platform/commit/9a5b9cbf76bff2342e1cb774fe3d6293c8199948))
* add typed teammate capability profile ([#2540](https://github.com/evalops/platform/issues/2540)) ([f968ab9](https://github.com/evalops/platform/commit/f968ab9f746f77023a46c346a158d542d48d76a6))
* **console:** deepen trace drilldown evidence ([#2774](https://github.com/evalops/platform/issues/2774)) ([14b7122](https://github.com/evalops/platform/commit/14b7122c0c30d11352e42dd4d47715ed48932ae6))
* **core:** add persisted Core API store ([#2563](https://github.com/evalops/platform/issues/2563)) ([6cbd7c6](https://github.com/evalops/platform/commit/6cbd7c6b6c5724ea16b43e271fdf457547aa26ca))
* **core:** add policy pack contract foundation ([#2549](https://github.com/evalops/platform/issues/2549)) ([f11a31c](https://github.com/evalops/platform/commit/f11a31c620884fda9df4c6166729cdfc7d70fa3a))
* **core:** add subject explanation readback ([#2573](https://github.com/evalops/platform/issues/2573)) ([c6fa736](https://github.com/evalops/platform/commit/c6fa736130328cc61894d6e45d6205e0d49852e9))
* deepen trace review payload parity ([#2754](https://github.com/evalops/platform/issues/2754)) ([d2e9ebb](https://github.com/evalops/platform/commit/d2e9ebb1c72d615b7fea67507ebd38831363fd37))
* expose A2A discovery evidence ([#2416](https://github.com/evalops/platform/issues/2416)) ([6c4c2b4](https://github.com/evalops/platform/commit/6c4c2b4d2fa9ba3ce0ab6d44f838ab9f6c1e90cb))
* implement Loop 5 triage, replay, and telemetry ([#2668](https://github.com/evalops/platform/issues/2668)) ([f38c2bc](https://github.com/evalops/platform/commit/f38c2bcf7a865618805b48c96745b7fd1df35408))
* surface native tool attempt runtime evidence ([#2858](https://github.com/evalops/platform/issues/2858)) ([96ff3cb](https://github.com/evalops/platform/commit/96ff3cba95191669f9281095d7341f0578087764))
* **traces:** add review annotations and MCP tools ([#2699](https://github.com/evalops/platform/issues/2699)) ([d0519ac](https://github.com/evalops/platform/commit/d0519ac06d4096f1808d29ccc2af7081ee4c9356))
* **traces:** add trace annotations ([#2692](https://github.com/evalops/platform/issues/2692)) ([25a0182](https://github.com/evalops/platform/commit/25a0182a1425d013d9df84c3c9c8e453cb83dc30))

## [0.1.593](https://github.com/evalops/platform/compare/gen/go/v0.1.592...gen/go/v0.1.593) (2026-06-03)


### Features

* add console authority posture ledger ([#2871](https://github.com/evalops/platform/issues/2871)) ([af00ae1](https://github.com/evalops/platform/commit/af00ae14ce19af3f19616e611078cde282664e61))

## [0.1.592](https://github.com/evalops/platform/compare/gen/go/v0.1.591...gen/go/v0.1.592) (2026-06-03)


### Features

* add console security decision packet ([#2866](https://github.com/evalops/platform/issues/2866)) ([ad1629d](https://github.com/evalops/platform/commit/ad1629dd6f6132837c700721669dfd194766a1f1))

## [0.1.591](https://github.com/evalops/platform/compare/gen/go/v0.1.590...gen/go/v0.1.591) (2026-06-03)


### Features

* add native agent event receipts ([#2863](https://github.com/evalops/platform/issues/2863)) ([dee014b](https://github.com/evalops/platform/commit/dee014b69e5216d307891ca073fe7e9fc609e423))
* surface native tool attempt runtime evidence ([#2858](https://github.com/evalops/platform/issues/2858)) ([96ff3cb](https://github.com/evalops/platform/commit/96ff3cba95191669f9281095d7341f0578087764))

## [0.1.590](https://github.com/evalops/platform/compare/gen/go/v0.1.589...gen/go/v0.1.590) (2026-05-31)


### Features

* add canonical trace review contract ([#2783](https://github.com/evalops/platform/issues/2783)) ([f0bff57](https://github.com/evalops/platform/commit/f0bff5707b62d43b45d211d41e72fbc36b12484b))

## [0.1.589](https://github.com/evalops/platform/compare/gen/go/v0.1.588...gen/go/v0.1.589) (2026-05-31)


### Features

* **console:** deepen trace drilldown evidence ([#2774](https://github.com/evalops/platform/issues/2774)) ([14b7122](https://github.com/evalops/platform/commit/14b7122c0c30d11352e42dd4d47715ed48932ae6))

## [0.1.588](https://github.com/evalops/platform/compare/gen/go/v0.1.587...gen/go/v0.1.588) (2026-05-31)


### Features

* **agentruntime:** add external-ref filtering to ListRunWaits for approval joins
* add Core status API and Slack parity ([#2584](https://github.com/evalops/platform/issues/2584)) ([e9425d7](https://github.com/evalops/platform/commit/e9425d758614024b0ba1fe7ee084a408ef040e41))
* add records service contract ([9a5b9cb](https://github.com/evalops/platform/commit/9a5b9cbf76bff2342e1cb774fe3d6293c8199948))
* **core:** add persisted Core API store ([#2563](https://github.com/evalops/platform/issues/2563)) ([6cbd7c6](https://github.com/evalops/platform/commit/6cbd7c6b6c5724ea16b43e271fdf457547aa26ca))
* **core:** add policy pack contract foundation ([#2549](https://github.com/evalops/platform/issues/2549)) ([f11a31c](https://github.com/evalops/platform/commit/f11a31c620884fda9df4c6166729cdfc7d70fa3a))
* **core:** add subject explanation readback ([#2573](https://github.com/evalops/platform/issues/2573)) ([c6fa736](https://github.com/evalops/platform/commit/c6fa736130328cc61894d6e45d6205e0d49852e9))
* deepen trace review payload parity ([#2754](https://github.com/evalops/platform/issues/2754)) ([d2e9ebb](https://github.com/evalops/platform/commit/d2e9ebb1c72d615b7fea67507ebd38831363fd37))
* implement Loop 5 triage, replay, and telemetry ([#2668](https://github.com/evalops/platform/issues/2668)) ([f38c2bc](https://github.com/evalops/platform/commit/f38c2bcf7a865618805b48c96745b7fd1df35408))
* **traces:** promote annotations into eval candidates ([#2737](https://github.com/evalops/platform/issues/2737)) ([b11e055](https://github.com/evalops/platform/commit/b11e055b7167a1b3244ca591fd7d291396504bfa))
* **traces:** add review annotations and MCP tools ([#2699](https://github.com/evalops/platform/issues/2699)) ([d0519ac](https://github.com/evalops/platform/commit/d0519ac06d4096f1808d29ccc2af7081ee4c9356))
* **traces:** add trace annotations ([#2692](https://github.com/evalops/platform/issues/2692)) ([25a0182](https://github.com/evalops/platform/commit/25a0182a1425d013d9df84c3c9c8e453cb83dc30))

## [0.1.587](https://github.com/evalops/platform/compare/gen/go/v0.1.586...gen/go/v0.1.587) (2026-05-25)


### Features

* add typed teammate capability profile ([#2540](https://github.com/evalops/platform/issues/2540)) ([f968ab9](https://github.com/evalops/platform/commit/f968ab9f746f77023a46c346a158d542d48d76a6))

## [0.1.586](https://github.com/evalops/platform/compare/gen/go/v0.1.585...gen/go/v0.1.586) (2026-05-20)


### Features

* expose A2A delegation graph ([#2371](https://github.com/evalops/platform/issues/2371)) ([aec9bb2](https://github.com/evalops/platform/commit/aec9bb20428651f19f355b16d9e75520b2cf49dc))
* expose A2A delegation read filters ([#2370](https://github.com/evalops/platform/issues/2370)) ([e9d9515](https://github.com/evalops/platform/commit/e9d95151de4d1ce3c82a996efce8d5c808f95a8d))
* expose A2A fleet discovery filters ([#2368](https://github.com/evalops/platform/issues/2368)) ([d2781b9](https://github.com/evalops/platform/commit/d2781b97f958073aea7a2896b983b3ddafdae2e1))
* expose A2A remote subagent wait contracts ([#2299](https://github.com/evalops/platform/issues/2299)) ([b7177be](https://github.com/evalops/platform/commit/b7177be99f31503740d94962ab17e9093885f972))

## [0.1.585](https://github.com/evalops/platform/compare/gen/go/v0.1.584...gen/go/v0.1.585) (2026-05-17)


### Features

* **agent-registry:** renew A2A delegation leases ([#2201](https://github.com/evalops/platform/issues/2201)) ([022cd12](https://github.com/evalops/platform/commit/022cd12c63458cfd11b85db59fd90c55948a78e2))

## [0.1.584](https://github.com/evalops/platform/compare/gen/go/v0.1.583...gen/go/v0.1.584) (2026-05-14)


### Features

* add Bazel build graph and GCP remote execution config ([a557cc1](https://github.com/evalops/platform/commit/a557cc1b21b8734a6613ab13233ecc75c44d72d8))

## [0.1.583](https://github.com/evalops/platform/compare/gen/go/v0.1.582...gen/go/v0.1.583) (2026-05-13)


### Features

* promote proactive runtime context ([#1968](https://github.com/evalops/platform/issues/1968)) ([83f1d3e](https://github.com/evalops/platform/commit/83f1d3e4211870950093b3faf0fba77278037653))


### Bug Fixes

* validate proactive retrieval counts ([#1973](https://github.com/evalops/platform/issues/1973)) ([80372f8](https://github.com/evalops/platform/commit/80372f8f25496210d16b1371436f3302754b5553))

## [0.1.582](https://github.com/evalops/platform/compare/gen/go/v0.1.581...gen/go/v0.1.582) (2026-05-13)


### Features

* **evalcontrol:** add server policy and canary gates ([#1958](https://github.com/evalops/platform/issues/1958)) ([df1ed36](https://github.com/evalops/platform/commit/df1ed3601d5a085d8716ceeb6aa2c29948ef6bbc))

## [0.1.581](https://github.com/evalops/platform/compare/gen/go/v0.1.580...gen/go/v0.1.581) (2026-05-13)


### Features

* add eval control service ([#1952](https://github.com/evalops/platform/issues/1952)) ([1400062](https://github.com/evalops/platform/commit/1400062d3b652c3e9734669a1c3a87dd2b3db378))
* Add durable channel thread adoption API ([#1944](https://github.com/evalops/platform/issues/1944)) ([e42b567](https://github.com/evalops/platform/commit/e42b5679ce2c3d29f3de5a1ab721e941b54d86c0))
* **agent-runtime:** expose VFS path capabilities ([#1945](https://github.com/evalops/platform/issues/1945)) ([cc204cd](https://github.com/evalops/platform/commit/cc204cd53bb29aa38ffba33f2ff544e654010548))
* **fermata:** add native evaluation packs ([c2e6a73](https://github.com/evalops/platform/commit/c2e6a732cf5a598db9d762157d190e3c203f2b51))
* scope vfs watch by selector ([4ff33eb](https://github.com/evalops/platform/commit/4ff33eb5571a9f405c4d3689631b5f43c966a635))
* merge VFS diff rebase release surface ([#1933](https://github.com/evalops/platform/issues/1933)) ([b888b03](https://github.com/evalops/platform/commit/b888b038513279db31d41626fe778629ba5d3269))
* **fermata:** harden trace replay and judge gates ([#1935](https://github.com/evalops/platform/issues/1935)) ([b3c30a3](https://github.com/evalops/platform/commit/b3c30a39a8516fb7193d61e7d6ccdb834c4f74f4))
* **agent-runtime:** add vfs transaction diff and rebase APIs ([34fd34c](https://github.com/evalops/platform/commit/34fd34cae939a62b0b7d28af5e17650a9a7f04ac))
* **fermata:** build trace suites from trace rpc ([#1929](https://github.com/evalops/platform/issues/1929)) ([bbc3732](https://github.com/evalops/platform/commit/bbc3732948a4e393ebf4a995f11c34c6dcb5d728))
* **agent-runtime:** support VFS tombstone operations ([5e0f2f4](https://github.com/evalops/platform/commit/5e0f2f4816660a1432daf232ed0edc7b7591f37b))
* **fermata:** make production trace suites replayable ([#1927](https://github.com/evalops/platform/issues/1927)) ([dee6190](https://github.com/evalops/platform/commit/dee61909fc196bbcd907a2b338d87241f1080191))
* **fermata:** add judge calibration reports ([#1924](https://github.com/evalops/platform/issues/1924)) ([52ea17a](https://github.com/evalops/platform/commit/52ea17aa9f3bd8afddfc81aad469e451b103ce83))
* **agent-runtime:** renew leases and harden VFS search ([#1922](https://github.com/evalops/platform/issues/1922)) ([91926c6](https://github.com/evalops/platform/commit/91926c65dc8a436536a2af7f99f6d5128126c4ec))
* **fermata:** index suite scenario runs ([#1921](https://github.com/evalops/platform/issues/1921)) ([ab95d83](https://github.com/evalops/platform/commit/ab95d8335372bc0a1e5ed37827d96d675aa56a0a))
* **agent-runtime:** add richer VFS search filters ([#1920](https://github.com/evalops/platform/issues/1920)) ([4aaf614](https://github.com/evalops/platform/commit/4aaf614055f12ce340da1e36fd5ecbcb37164727))
* **fermata:** add native suite rerun filters ([#1919](https://github.com/evalops/platform/issues/1919)) ([7cdde8d](https://github.com/evalops/platform/commit/7cdde8db60dfef2b879e2462b853ce088ab4604e))
* **fermata:** add advisory LLM judge mode ([#1917](https://github.com/evalops/platform/issues/1917)) ([792c32b](https://github.com/evalops/platform/commit/792c32b254868519ab0db80d07ab923c02a22274))
* **vfs:** include redaction state in events ([#1914](https://github.com/evalops/platform/issues/1914)) ([65b011d](https://github.com/evalops/platform/commit/65b011d70b747a1801c24e1fd8c5323e780cf98d))
* **agent-runtime:** add VFS redaction state ([#1912](https://github.com/evalops/platform/issues/1912)) ([89b0adc](https://github.com/evalops/platform/commit/89b0adcf5edb367eb80809c2a348c40ac965c47b))
* **fermata:** add native agent trajectory assertions ([#1909](https://github.com/evalops/platform/issues/1909)) ([96a4e1d](https://github.com/evalops/platform/commit/96a4e1dbb17f65e4b268a078c86512ed3df0805b))
* **agent-runtime:** add VFS watch stream ([#1906](https://github.com/evalops/platform/issues/1906)) ([334d6f5](https://github.com/evalops/platform/commit/334d6f54c3181298a36158a6115d028964eac3eb))
* **agent-runtime:** expose VFS provenance ([#1905](https://github.com/evalops/platform/issues/1905)) ([fb6d70b](https://github.com/evalops/platform/commit/fb6d70b5a59c4b192f578399f8968230ad5b0e7c))
* **agent-runtime:** add VFS context packs ([#1904](https://github.com/evalops/platform/issues/1904)) ([063ca81](https://github.com/evalops/platform/commit/063ca817e93bccd00147a30821f109a120ab23c4))
* **fermata:** add pairwise LLM rubric judges ([#1901](https://github.com/evalops/platform/issues/1901)) ([7a4ea9c](https://github.com/evalops/platform/commit/7a4ea9c64f03f55b1b42743791140f4d27f77cce))

## [0.1.580](https://github.com/evalops/platform/compare/gen/go/v0.1.579...gen/go/v0.1.580) (2026-05-12)


### Features

* add calibrated llm rubric judges ([#1884](https://github.com/evalops/platform/issues/1884)) ([28b8a93](https://github.com/evalops/platform/commit/28b8a9387ce5d4ca3fbe1b3255cd0787eecb9ae4))

## [0.1.579](https://github.com/evalops/platform/compare/gen/go/v0.1.578...gen/go/v0.1.579) (2026-05-12)


### Features

* add owned CRM surface to pipeline ([#1821](https://github.com/evalops/platform/issues/1821)) ([58c4488](https://github.com/evalops/platform/commit/58c448871f18cb5f3ab6af5861bbbc0761e205f6))

## [0.1.578](https://github.com/evalops/platform/compare/gen/go/v0.1.577...gen/go/v0.1.578) (2026-05-11)


### Features

* add standalone VFS service and agent tools ([#1796](https://github.com/evalops/platform/issues/1796)) ([6da6b60](https://github.com/evalops/platform/commit/6da6b60e4d37b8fef966ea85f05d9a59b52fce32))

## [0.1.577](https://github.com/evalops/platform/compare/gen/go/v0.1.576...gen/go/v0.1.577) (2026-05-10)


### Features

* add run-scoped connector grant plans ([#1625](https://github.com/evalops/platform/issues/1625)) ([25861a1](https://github.com/evalops/platform/commit/25861a1682053c63642036dfb7d54a3fcc9b00e8))
* filter run waits by external ref ([#1678](https://github.com/evalops/platform/issues/1678)) ([1279831](https://github.com/evalops/platform/commit/1279831219f132145ea40c0d40a233b75892a913))


### Bug Fixes

* harden agent runtime virtual files ([#1656](https://github.com/evalops/platform/issues/1656)) ([4f44f84](https://github.com/evalops/platform/commit/4f44f845da4257ba9f400aa3b436c8fabff8cc6e))
* harden Slack continuation adoption ([#1634](https://github.com/evalops/platform/issues/1634)) ([fe7b8dd](https://github.com/evalops/platform/commit/fe7b8dd2f2ba8f44e0a36ed37e61f56206e0a89d))
* harden teammate work ledger refresh ([#1644](https://github.com/evalops/platform/issues/1644)) ([ae8ebba](https://github.com/evalops/platform/commit/ae8ebba410945c5c16dc951aff6f19e43174e95f))
* make visual action grounding safety presence-aware ([#1654](https://github.com/evalops/platform/issues/1654)) ([3a20c06](https://github.com/evalops/platform/commit/3a20c06b60a3a5d0161d0fcea43314991afd8c60))

## [0.1.576](https://github.com/evalops/platform/compare/gen/go/v0.1.575...gen/go/v0.1.576) (2026-05-08)


### Features

* **agentruntime:** add adapter-observed runtime events ([31fb721](https://github.com/evalops/platform/commit/31fb7214261a445dce0d0c9b317cbce0d58fd41e))
* **agentruntime:** add runtime channel actor identity fields ([#1548](https://github.com/evalops/platform/issues/1548)) ([48bc720](https://github.com/evalops/platform/commit/48bc72063529c8e91df054002ca6f9d5a094d663))
* **agentruntime:** add VFS and connector provider catalog ([806a1c9](https://github.com/evalops/platform/commit/806a1c989a4233666e44c3d72d0597cbbe932476))
* **proto:** add browser-control receipt taxonomy ([0ed252e](https://github.com/evalops/platform/commit/0ed252ec1072ba41ebfe49820427006a0d2736d0))
* **agentruntime:** add durable VFS tools and proposals ([1166d22](https://github.com/evalops/platform/commit/1166d22cf3982044e1f73e58c2fabdb79e7e789c))
* **agentruntime:** add versioned VFS transactions ([#1573](https://github.com/evalops/platform/issues/1573)) ([7be0419](https://github.com/evalops/platform/commit/7be0419eba50f7c3df84de7525857a53f2ae9188))

## [0.1.575](https://github.com/evalops/platform/compare/gen/go/v0.1.574...gen/go/v0.1.575) (2026-05-05)


### Bug Fixes

* address missed platform review feedback ([#1502](https://github.com/evalops/platform/issues/1502)) ([c3eadd8](https://github.com/evalops/platform/commit/c3eadd8d82d894ea66786e08ff224b171d8f3a6b))

## [0.1.574](https://github.com/evalops/platform/compare/gen/go/v0.1.573...gen/go/v0.1.574) (2026-05-05)


### Features

* add AI operations console surface ([#1481](https://github.com/evalops/platform/issues/1481)) ([df22ca6](https://github.com/evalops/platform/commit/df22ca6b61b267b9462c4a1e49a7d701c99eec11))
* add console evals, costs, and Maestro trace ingestion ([f5937db](https://github.com/evalops/platform/commit/f5937dbf936f6eded1424af496d4f0cf3b7ec8fa))
* wire console global filters ([e787359](https://github.com/evalops/platform/commit/e78735906e493b5b5dd1d7888aa1f718e75fc87d))

## [0.1.573](https://github.com/evalops/platform/compare/gen/go/v0.1.572...gen/go/v0.1.573) (2026-05-04)


### Features

* **identity:** add current user proto surface ([fb19021](https://github.com/evalops/platform/commit/fb19021ebd4e18c3bd9caa8aae7d40298bf681b9))
* **ui:** build live agent governance dashboard ([32b3b47](https://github.com/evalops/platform/commit/32b3b47df891f75999ab626d912a065112442c48))

## [0.1.572](https://github.com/evalops/platform/compare/gen/go/v0.1.571...gen/go/v0.1.572) (2026-05-03)


### Features

* add Maestro learned context event contract ([#1411](https://github.com/evalops/platform/issues/1411)) ([007cbf0](https://github.com/evalops/platform/commit/007cbf00c1cc5b17c26e70ad4ec397da58c63bc6))
* add org user trace attribution ([#1407](https://github.com/evalops/platform/issues/1407)) ([196f33a](https://github.com/evalops/platform/commit/196f33a9e4fd4555eae0911ffd55d6698c3d7d6d))

## [0.1.571](https://github.com/evalops/platform/compare/gen/go/v0.1.570...gen/go/v0.1.571) (2026-05-01)


### Features

* replace ingest ClickHouse sink with BigQuery ([5856d97](https://github.com/evalops/platform/commit/5856d97c992a9a541d74c0016ee96714757edb46))
