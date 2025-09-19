package cmd

import (
	
	"github.com/spf13/cobra"
	
)

var rootCmd = &cobra.Command{
	Use: "connector",
	Short: "A connector for a semantic catalog interacting with Trino",
	Long: "this connector is how we connect the Semantic search catalog to trino",


}


func Execute() error{
	return rootCmd.Execute()
	
	}

