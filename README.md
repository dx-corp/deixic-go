# Deixic SDK for Go

This repository is the generated Go client for Deixic's public API. Its source
of truth is `dx-corp/mono`; the standalone repository is a deterministic
projection of the explicitly public `deixicpublic.v1` protocol. Its only
protocol dependency is the Protobuf well-known `Timestamp` type.

## Install

```sh
go get github.com/dx-corp/deixic-go/deixicpublic/v1/deixicpublicv1connect
```

Create a Connect client with the generated Deixic service package:

```go
package main

import (
	"net/http"

	"github.com/dx-corp/deixic-go/deixicpublic/v1/deixicpublicv1connect"
)

func main() {
	client := deixicpublicv1connect.NewDeixicPublicServiceClient(
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
made in Mono's `proto/deixicpublic/v1/` tree and regenerated there. The
projection contains only this reviewed public schema and its client.
