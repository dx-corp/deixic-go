package deixicv1connect_test

import (
	"testing"

	"github.com/dx-corp/deixic-go/deixic/v1/deixicv1connect"
)

func TestProjectedServiceIdentity(t *testing.T) {
	if got, want := deixicv1connect.DeixicServiceName, "deixic.v1.DeixicService"; got != want {
		t.Fatalf("service name = %q, want %q", got, want)
	}
	if got, want := deixicv1connect.DeixicServiceSubmitOperatingMessageProcedure,
		"/deixic.v1.DeixicService/SubmitOperatingMessage"; got != want {
		t.Fatalf("submit procedure = %q, want %q", got, want)
	}
}
