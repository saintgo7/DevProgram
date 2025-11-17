// Texture

#include "Program069.h"

AProgram069::AProgram069()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AProgram069::BeginPlay()
{
    Super::BeginPlay();

    UE_LOG(LogTemp, Warning, TEXT("=== Texture ==="));
    UE_LOG(LogTemp, Warning, TEXT("This is an Unreal C++ program demonstrating texture."));

    // Implement the program logic here...
}

void AProgram069::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Tick logic here...
}
