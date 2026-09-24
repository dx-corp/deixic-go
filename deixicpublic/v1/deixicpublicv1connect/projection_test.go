package deixicpublicv1connect_test

import (
	"testing"

	"github.com/dx-corp/deixic-go/deixicpublic/v1/deixicpublicv1connect"
)

func TestProjectedServiceIdentity(t *testing.T) {
	if got, want := deixicpublicv1connect.DeixicPublicServiceName, "deixicpublic.v1.DeixicPublicService"; got != want {
		t.Fatalf("service name = %q, want %q", got, want)
	}
	if got, want := deixicpublicv1connect.DeixicPublicServiceSubmitTaskProcedure,
		"/deixicpublic.v1.DeixicPublicService/SubmitTask"; got != want {
		t.Fatalf("submit procedure = %q, want %q", got, want)
	}
}
