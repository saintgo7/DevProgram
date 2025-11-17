// Cascade
// Program 073

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program073.generated.h"

UCLASS()
class AProgram073 : public AActor
{
    GENERATED_BODY()

public:
    AProgram073();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
