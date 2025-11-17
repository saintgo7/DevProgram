// Camera Component

#include "Program082.h"

AProgram082::AProgram082()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram082::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Camera Component ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating camera component."));

    // Implement the program logic here...
}

void AProgram082::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
