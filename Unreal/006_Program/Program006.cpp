// Movement Component

#include "Program006.h"

AProgram006::AProgram006()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram006::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Movement Component ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating movement component."));

    // Implement the program logic here...
}

void AProgram006::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
