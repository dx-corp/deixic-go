package main

import (
	"fmt"
	"os"
	"sort"

	_ "github.com/dx-corp/deixic-go/deixicpublic/v1"
	"google.golang.org/protobuf/reflect/protoreflect"
	"google.golang.org/protobuf/reflect/protoregistry"
)

func main() {
	var files []string
	var violations []string
	protoregistry.GlobalFiles.RangeFiles(func(file protoreflect.FileDescriptor) bool {
		files = append(files, file.Path())
		return true
	})
	sort.Strings(files)
	for _, name := range files {
		if name != "deixicpublic/v1/sdk.proto" && name != "google/protobuf/timestamp.proto" {
			violations = append(violations, "unexpected descriptor: "+name)
		}
	}
	public, err := protoregistry.GlobalFiles.FindFileByPath("deixicpublic/v1/sdk.proto")
	if err != nil {
		violations = append(violations, "public descriptor is missing")
	} else {
		if string(public.Package()) != "deixicpublic.v1" {
			violations = append(violations, "unexpected public proto package")
		}
		if public.Imports().Len() != 1 || public.Imports().Get(0).Path() != "google/protobuf/timestamp.proto" {
			violations = append(violations, "unexpected public descriptor import closure")
		}
		if public.Services().Len() != 1 || string(public.Services().Get(0).Name()) != "DeixicPublicService" {
			violations = append(violations, "unexpected public service set")
		}
	}
	if len(violations) != 0 {
		for _, violation := range violations {
			fmt.Fprintln(os.Stderr, violation)
		}
		os.Exit(1)
	}
	fmt.Printf("public descriptor closure: %v\n", files)
}
