# PowerShell Profile - Add this to the file
function Show-Tree {
    param (
        [string]$Path = ".",
        [string]$Indent = "",
        [string[]]$Exclude = @('trading_env', '__pycache__', '.git', 'node_modules', '.pytest_cache', 'data'),
        [int]$MaxDepth = 10,
        [int]$CurrentDepth = 0
    )
    
    # Check if path exists
    if (-not (Test-Path $Path)) {
        Write-Warning "Path '$Path' does not exist."
        return
    }
    
    # Prevent infinite recursion
    if ($CurrentDepth -ge $MaxDepth) {
        return
    }
    
    try {
        # Get items with error handling
        $items = Get-ChildItem $Path -Force -ErrorAction Stop | Where-Object { 
            $_.Name -notin $Exclude -and -not $_.Name.StartsWith('.')
        } | Sort-Object @{Expression={$_.PSIsContainer}; Descending=$true}, Name
        
        # Handle empty directories
        if ($items.Count -eq 0) {
            return
        }
        
        for ($i = 0; $i -lt $items.Count; $i++) {
            $item = $items[$i]
            $isLast = ($i -eq $items.Count - 1)
            $prefix = if ($isLast) { "└── " } else { "├── " }
            
            # Use Write-Host for better formatting control
            Write-Host "$Indent$prefix$($item.Name)" -NoNewline
            
            # Add file size for files
            if (-not $item.PSIsContainer) {
                $size = if ($item.Length -lt 1KB) { 
                    "$($item.Length) B" 
                } elseif ($item.Length -lt 1MB) { 
                    "{0:N1} KB" -f ($item.Length / 1KB) 
                } else { 
                    "{0:N1} MB" -f ($item.Length / 1MB) 
                }
                Write-Host " ($size)" -ForegroundColor Gray
            } else {
                Write-Host ""
            }
            
            # Recurse into directories
            if ($item.PSIsContainer) {
                $newIndent = if ($isLast) { "$Indent    " } else { "$Indent│   " }
                Show-Tree -Path $item.FullName -Indent $newIndent -Exclude $Exclude -MaxDepth $MaxDepth -CurrentDepth ($CurrentDepth + 1)
            }
        }
    }
    catch {
        Write-Warning "Error accessing '$Path': $($_.Exception.Message)"
    }
}

# Alias for convenience
Set-Alias -Name tree -Value show-tree