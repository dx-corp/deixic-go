# Deixic SDK for Go

This repository is the generated Go client for Deixic's public API. Its source
of truth is `dx-corp/mono`; the standalone repository is a deterministic
projection of the Deixic service descriptor and its generated dependency
closure.

## Install

```sh
go get github.com/dx-corp/deixic-go/deixic/v1/deixicv1connect
```

Create a Connect client with the generated Deixic service package:

```go
package main

import (
	"net/http"

	"github.com/dx-corp/deixic-go/deixic/v1/deixicv1connect"
)

func main() {
	client := deixicv1connect.NewDeixicServiceClient(
		http.DefaultClient,
		"https://app.deixic.com",
	)
	_ = client
}
```

Callers must supply their Deixic authentication and tenant-scope headers. The
generated client does not invent organization, workspace, authorization, or
idempotency values.

## Source and releases

Do not edit generated files in the standalone repository. Contract changes are
made in Mono's `proto/` tree and regenerated there. The projection copies only
the Deixic service package and the generated packages required to compile it;
it does not publish Mono's full generated tree.
