// Blend Space
// Program 034

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program034.generated.h"

UCLASS()
class AProgram034 : public AActor
{
    GENERATED_BODY()

public:
    AProgram034();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
