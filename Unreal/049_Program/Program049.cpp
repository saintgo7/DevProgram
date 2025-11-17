// HUD

#include "Program049.h"

AProgram049::AProgram049()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram049::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== HUD ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating hud."));

    // Implement the program logic here...
}

void AProgram049::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
