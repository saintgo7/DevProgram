// Texture
// Program 069

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program069.generated.h"

UCLASS()
class AProgram069 : public AActor
{
    GENERATED_BODY()

public:
    AProgram069();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
