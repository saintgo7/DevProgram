// Camera Component
// Program 082

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program082.generated.h"

UCLASS()
class AProgram082 : public AActor
{
    GENERATED_BODY()

public:
    AProgram082();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
