package cmd

import (
	"fmt"
	"os"
	"github.com/spf13/cobra"
	
)

var rootCmd = &cobra.Command{
	Use: "connector",
	Short: "A connector for a semantic catalog interacting with Trino",
	Long: "this connector is how we connect the Semantic search catalog to trino",


}


func Execute() {
	if err := rootCMD.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
