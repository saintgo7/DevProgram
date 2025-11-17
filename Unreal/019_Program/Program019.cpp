// UStaticMeshComponent

#include "Program019.h"

AProgram019::AProgram019()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram019::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== UStaticMeshComponent ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating ustaticmeshcomponent."));

    // Implement the program logic here...
}

void AProgram019::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
